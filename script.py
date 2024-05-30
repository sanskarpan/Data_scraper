import requests
import logging
import pymongo
from concurrent.futures import ThreadPoolExecutor
from json.decoder import JSONDecodeError

logging.basicConfig(filename='scrap.log', level=logging.ERROR)
TIMEOUT = 10

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["scraping_db"]
collection = db["scraped_data"]

def fetch_data(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status() 
        content_type = response.headers.get('Content-Type', '')
        if content_type.startswith('application/json'):
            data = parse_ajax_response(response)
        elif content_type.startswith('text/html'):
            data = parse_html_response(response, url)
        else:
            logging.error(f"Unexpected content type for {url}: {content_type}")
            return None
        return url, data        

    except requests.exceptions.Timeout as e:
        logging.error(f"Timeout error fetching {url}: {e}")
        return None
    except requests.exceptions.ConnectionError as e:
        logging.error(f"Connection error fetching {url}: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error fetching {url}: {e}")
        return None
    except JSONDecodeError as e:
        logging.error(f"Error parsing JSON data for {url}: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error fetching {url}: {e}")
        return None

def parse_ajax_response(response):
    try:
        json_data = response.json()
        return json_data
    except JSONDecodeError as e:
        logging.error(f"Error parsing JSON data: {e}")
        return None

def parse_html_response(response, url):
    try:           
        return response.text
    except Exception as e:
        logging.error(f"Error parsing HTML data: {e}")
        return None

def save_to_mongodb(url, data):
    if data:
        try:
            collection.insert_one({"url": url, "data": data})
        except Exception as e:
            logging.error(f"Error saving data to MongoDB: {e}")

def scrape_urls(urls):
    print("Scraping started...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_data, url) for url in urls]
        for url, future in zip(urls, futures):
            try:
                result = future.result()
                if result:
                    url, cleaned_data = result
                    save_to_mongodb(url, cleaned_data)
                    print(f"Data scraped from {url} and stored in MongoDB.")
                else:
                    print(f"Failed to scrape data from {url}.")
            except Exception as e:
                logging.error(f"Error processing {url}: {e}")

urls = [
    "https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015",
    "https://www.scrapethissite.com/pages/forms/",
    "https://www.scrapethissite.com/pages/advanced/"
]
scrape_urls(urls)
print("Scraping completed.")