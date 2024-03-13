# Google-Maps-Scrapper
This Python script amalgamates web scraping and fuzzy matching for extracting potential company names from website HTML, and employs the Google Maps API to find location details based on the company's name, offering a comprehensive solution for gathering and validating company information from online sources. 
## maps_scrapper.py 
This Python script leverages the Google Maps API to retrieve the location details of a company based on its name.
Reads the company names from a CSV file (companyName_file.csv).Selects the first company name for processing.
Google Maps Geocoding:Utilizes the Google Maps Geocoding API to obtain the latitude and longitude of the company's location.
Places API Search:Utilizes the obtained coordinates to search for the company using the Google Places API.Retrieves information such as the company name and formatted address.

## scrappin.py
This Python script combines web scraping and fuzzy matching techniques to extract potential company names from the HTML content of a website.
Reads the domain addresses from a CSV file (output_data.csv).Selects a specific domain address for processing (address_list[19]).
HTTP Request and HTML Parsing:Uses the requests library to make an HTTP request to the specified URL.Utilizes BeautifulSoup to parse the HTML content of the website.
Company Name Extraction:Searches for a specific HTML element (span with class company-name) to extract the company name.
Performs fuzzy matching against the words in the HTML content to identify potential matches with the selected domain.

## scrapping.py
Coded an alternate method for address scrapping.
This Python script performs web scraping to extract company addresses by following these steps:
Reads domain addresses from a CSV file (output_data.csv).Selects a specific domain address for processing (address_list[1]).
Sets up a retry mechanism using the requests.adapters module to handle potential connection issues.
Sends an HTTP GET request to the specified URL (https:// + address_list[1]) with a timeout of 1 second.
Raises an HTTPError for bad responses (4xx and 5xx).Uses BeautifulSoup to parse the HTML content of the response.
Finds all <a> (anchor) elements with an href attribute using BeautifulSoup.
Extracts 'about-us' links from the list of links.
Extracting Address from 'About Us' Page:Checks if 'about-us' links are present.
If present, selects the second link (about_us_links[1]) and sends an HTTP GET request to fetch the 'about us' page content.
Uses BeautifulSoup to parse the HTML content and finds the <span> element with the class contact-text.Extracts the address from the contact span and prints it to the console.

## Problems I encountered and hope to find a method
The list of urls contains 2042 elements. Very few have a similar html structure , so I could not do a general case for scrapping. That is why the scripts run only on a single case.
