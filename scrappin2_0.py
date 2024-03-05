import time
import csv
import requests
import pandas as pd
import re
from urllib.parse import urlparse
from fuzzywuzzy import fuzz
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup



df = pd.read_csv('output_data.csv')
address_list = df['domain'].tolist()
address_list_element = address_list[19]
url = 'https://' + address_list_element


retries = Retry(total=1, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
http = requests.Session()
http.mount("https://", adapter)

try:
    response = http.get(url, timeout=10)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    company_name_element = soup.find('span', class_='company-name')
    
    # Find all links
    links = soup.find_all('a', href=True)
    
    if company_name_element:
        company_name = company_name_element.text.strip()
        print(company_name)
    
    all_text = soup.get_text()
    
    similarity_threshold = 40 # Adjust the threshold as needed
    
    matched_words = []

    for word in all_text.split():
        similarity_score = fuzz.ratio(word.lower(), address_list_element.lower())
        if similarity_score > similarity_threshold:
            matched_words.append(word.strip())
             
    
    unique_words = list(set(matched_words))
    
    result_string = ' '.join(matched_words)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    csv_file_path = f'companyName_file.csv'
    df = pd.DataFrame([result_string], columns=['company_name'])
    df.to_csv(csv_file_path, index=False)

except requests.exceptions.RequestException as e:
    print(f"Error accessing {url}: {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTPError for {url}: {e}")