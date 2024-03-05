import googlemaps
import time
import csv
import re
import requests
import usaddress
import pandas as pd
from urllib.parse import urlencode
from urllib.request import urlparse 
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup


#Read the csv file
csv_file_path = 'companyName_file.csv'
df = pd.read_csv(csv_file_path)
company_names = df['company_name'].tolist()
company_name = company_names[0]



url = 'https://' + company_name

# parsed_url = urlparse(url)
# company_name = get_company_name1(url)





api_key = "AIzaSyCH3-GzvWwPUkFka3z-YxTnQsWArKCN1Lk"
gmaps = googlemaps.Client(key=api_key)
geocoding_result = gmaps.geocode(company_name)


result_dict = {}  # Create an empty dictionary to store the results

if geocoding_result:
    location = geocoding_result[0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']

    # Use the Places API to search for the company with a location bias
    places_result = gmaps.places(query=company_name, location=f"{latitude},{longitude}")

    # Check if any results are found
    if places_result['status'] == 'OK' and places_result.get('results'):
        # Get the first result
        first_result = places_result['results'][0]

        # Extract information, such as name, address, etc.
        name = first_result.get('name', 'N/A')
        formatted_address = first_result.get('formatted_address', 'N/A')

        csv_file_path = f'result_file.csv'
        df = pd.DataFrame({'company_name': [name], 'address': [formatted_address.strip()]})
        df.to_csv(csv_file_path, index=False)
        # Store the results in the dictionary
        result_dict['Company Name'] = name
        result_dict['Address'] = formatted_address.strip()
    else:
        result_dict['Error'] = f"No results found for '{company_name}' near the specified location."
else:
    result_dict['Error'] = f"Unable to retrieve the location for '{company_name}'."




