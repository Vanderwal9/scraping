import requests
import time


api_key = 'api key'
# Base URL for Google Places text search
url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# Queries for different types of restaurants
queries = [
    'latino construction near me',
    'hispanic construction near me',




    # Add more queries
]

all_places = [] 
seen_names = set()  # To track names and filter out duplicates by name, not address

for query in queries:
    print(f"Searching for: {query}")
    
    next_page_token = None
    while True:
        # Parameters for the text search
        params = {
            'query': query,
            'key': api_key,
            'pagetoken': next_page_token  # Handle pagination
        }

        response = requests.get(url, params=params)
        results = response.json()

        if results.get('status') != 'OK':
            print(f"Error fetching data for '{query}': {results.get('error_message', 'Unknown error')}")
            break  

        for place in results['results']:
            name = place.get('name')
            
            if name not in seen_names:
                seen_names.add(name)  # Mark this name as seen

                place_id = place.get('place_id')

               
                details_url = "https://maps.googleapis.com/maps/api/place/details/json"
                details_params = {
                    'place_id': place_id,
                    'fields': 'formatted_phone_number,website',
                    'key': api_key
                }

                details_response = requests.get(details_url, params=details_params)
                details_results = details_response.json()

                phone_number = details_results.get('result', {}).get('formatted_phone_number', 'No phone number')
                website = details_results.get('result', {}).get('website', 'No website')

                all_places.append({
                    'name': name,
                    'address': place.get('formatted_address'),
                    'phone_number': phone_number,
                    'website': website
                })

        next_page_token = results.get('next_page_token')
        if not next_page_token:
            break  
        time.sleep(2)  # Ensure compliance with Google's rate limiting

# Print or process all gathered information
for place in all_places:
    print(f"{place['name']}, {place['address']}, {place['phone_number']}, {place['website']}")


# Now, convert the collected data into a DataFrame and export it to an Excel file
import pandas as pd

df = pd.DataFrame(all_places)
excel_file_path = 'constructions.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print('Excel file has been created successfully.')

