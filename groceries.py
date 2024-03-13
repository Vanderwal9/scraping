import requests
import time


api_key = 'apikey'
# Base URL for Google Places text search
url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# Queries for different types of restaurants
queries = [
    'Latino grocery stores in Washington DC',
'Mexican grocery stores in Washington DC',
'Cuban grocery stores in Washington DC',
'Chilean grocery stores in Washington DC',
'Venezuelan grocery stores in Washington DC',
'Latino grocery stores in the DMV',
'Mexican grocery stores in the DMV',
'Uruguayan grocery stores in the DMV',
'Puerto Rican grocery stores in the DMV',
'Puerto Rican grocery stores in Washington DC',
'Belizean grocery stores in Washington DC',
'Costa Rican grocery stores in Washington DC',
'Salvadorian grocery stores in Washington DC',
'Guatemalan grocery stores in Washington DC',
'Honduran grocery stores in Washington DC',
'Nicaraguan grocery stores in Washington DC',
'Panamanian grocery stores in Washington DC',
'Argentinian grocery stores in Washington DC',
'Bolivian grocery stores in Washington DC',
'Brazilian grocery stores in Washington DC',
'Chilean grocery stores in Washington DC',
'Colombian grocery stores in Washington DC',
'Ecuadorian grocery stores in Washington DC',
'Guyanese grocery stores in Washington DC',
'Paraguayan grocery stores in Washington DC',
'Peruvian grocery stores in Washington DC',
'Surinamese grocery stores in Washington DC',
'Uruguayan grocery stores in Washington DC',
'Venezuelan grocery stores in Washington DC',
'Belizean grocery stores in the DMV',
'Costa Rican grocery stores in the DMV',
'Salvadorian grocery stores in the DMV',
'Guatemalan grocery stores in the DMV',
'Honduran grocery stores in the DMV',
'Nicaraguan grocery stores in the DMV',
'Panamanian grocery stores in the DMV',
'Argentinian grocery stores in the DMV',
'Bolivian grocery stores in the DMV',
'Brazilian grocery stores in the DMV',
'Chilean grocery stores in the DMV',
'Colombian grocery stores in the DMV',
'Ecuadorian grocery stores in the DMV',
'Guyanese grocery stores in the DMV',
'Paraguayan grocery stores in the DMV',
'Peruvian grocery stores in the DMV',
'Surinamese grocery stores in the DMV',
'Uruguayan grocery stores in the DMV',
'Venezuelan grocery stores in the DMV',




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
        time.sleep(1)  # Ensure compliance with Google's rate limiting

# Print or process all gathered information
for place in all_places:
    print(f"{place['name']}, {place['address']}, {place['phone_number']}, {place['website']}")


# Now, convert the collected data into a DataFrame and export it to an Excel file
import pandas as pd

df = pd.DataFrame(all_places)
excel_file_path = 'grocery.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print('Excel file has been created successfully.')

