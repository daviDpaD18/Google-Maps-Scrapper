import time
import csv
import requests
import pandas as pd
import re
from urllib.parse import urlparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup




# Read CSV file and extract the 'domain' column
df = pd.read_csv('output_data.csv')
address_list = df['domain'].tolist()



# Set up retry mechanism
retries = Retry(total=1, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
http = requests.Session()
http.mount("https://", adapter)

url = 'https://' + address_list[1]
url_title = urlparse(url).netloc


# Set up retry mechanism
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
http = requests.Session()
http.mount("https://", adapter)


try:
    response = http.get(url, timeout=1)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links
    links = soup.find_all('a', href=True)
    
    # Extract 'about-us' links
    about_us_links = [link['href'] for link in links if 'about-us' in link['href']]
    
    if about_us_links:
        about_us_url = about_us_links[1]
        about_us_response = http.get(about_us_url, timeout=1)

        if about_us_response.status_code == 200:
            about_us_soup = BeautifulSoup(about_us_response.text, 'html.parser')
            contact_span = about_us_soup.find('span', class_='contact-text')
            address = contact_span.get_text(strip=True)
            print(address)
            

       
        

except requests.exceptions.RequestException as e:
    print(f"Error accessing {url}: {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTPError for {url}: {e}")