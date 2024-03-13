import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Load URLs from an Excel file
input_file = 'restaurants.xlsx'  # Ensure this is the correct path to your file
df = pd.read_excel(input_file)

# Define a simple regex for finding email addresses
email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'

# Function to scrape emails from a single URL
def scrape_emails(url):
    # print(f"Processing: {url}")  # Feedback to indicate which URL is being processed
    try:
        response = requests.get(url, timeout=10)
        emails = re.findall(email_regex, response.text)
        email_result = ", ".join(set(emails)) if emails else "No email found"
        print(f"Done: {url}")  # Feedback when finishing processing a URL
        return email_result
    except requests.RequestException as e:
        print(f"Failed to retrieve: {url}")  # Feedback for failed retrieval
        return "Failed to retrieve"

# Apply the scraping function to each URL in the DataFrame
df['Emails'] = df['website'].apply(scrape_emails)

# Save the results to a new Excel file
output_file = 'emails.xlsx'  # Ensure you have the correct output file path
df.to_excel(output_file, index=False, engine='openpyxl')

print('Scraping complete. Results saved to:', output_file)
