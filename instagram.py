import pandas as pd
from bs4 import BeautifulSoup
import requests

def find_social_media_links(url):
    """
    Function to find the Instagram link on a given website.
    :param url: URL of the website to search.
    :return: Instagram URL if found, None otherwise.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Search for Instagram links. This might need adjustments for specific site structures.
            for link in soup.find_all('a', href=True):
                if 'instagram.com' in link['href']:
                    return link['href']
    except Exception as e:
        print(f"Error accessing {url}: {e}")
    return None

def main():
    # Load the Excel file
    df = pd.read_excel('resturants for instagram.xlsx', engine='openpyxl')

    # Assuming the column with website URLs is named 'website'
    df['instagram'] = df['website'].apply(lambda x: find_social_media_links(x) if pd.notna(x) else None)

    # Save the updated DataFrame back to an Excel file
    df.to_excel('updated_restaurants.xlsx', index=False, engine='openpyxl')
    print('Updated Excel file has been created successfully with Instagram links.')

if __name__ == "__main__":
    main()
