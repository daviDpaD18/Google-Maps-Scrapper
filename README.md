# Google-Maps-Scrapper
This Python script amalgamates web scraping and fuzzy matching for extracting potential company names from website HTML, and employs the Google Maps API to find location details based on the company's name, offering a comprehensive solution for gathering and validating company information from online sources.
## maps_scrapper.py 
This Python script leverages the Google Maps API to retrieve the location details of a company based on its name.
Reads the company names from a CSV file (companyName_file.csv).Selects the first company name for processing.
Google Maps Geocoding:Utilizes the Google Maps Geocoding API to obtain the latitude and longitude of the company's location.
Places API Search:Utilizes the obtained coordinates to search for the company using the Google Places API.Retrieves information such as the company name and formatted address.
