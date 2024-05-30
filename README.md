# Scraping Application

## Introduction
This Python scraping application is able to scrape data concurrently from different URLs, process data both from JSON and HTML, and save scraped data in a MongoDB database effectively. Some of the major features are strong error handling, customizable thread pool management for optimum scraping, and complete logging for debugging. The application is versatile, meaning that it should fit most scraping requirements—from market research and competitive analytics to automated data retrieval tasks. This application, considering performance optimization with its features, gives an optimal solution to users looking for ease in gathering and storing structured data from the web.
## Key Features
- **Concurrent Scraping**
- **Content-Type Handling**
- **Error Handling and Logging**
- **Data Persistence**
- **Performance Optimization**


## Dependencies
- Python 3.6 or later
- Requests library
- pymongo library
- MongoDB server
## Installation
1. **Python**: If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).
2. **Requests Library**: Install the Requests library using pip:
```bash
pip install requests
```
3. **pymongo Library**: Install the pymongo library using pip:
```bash
pip install pymongo
```
## Setup
1. **MongoDB**: Ensure that MongoDB is installed and running on your system. If not, download and install it from the [official MongoDB website](https://www.mongodb.com/try/download/community).
2. **Database Configuration**: By default, the application connects to a MongoDB instance running on `localhost` at port `27017`. If your MongoDB instance is running on a different host or port, modify the connection string accordingly in the code (`scrape.py`).

## Usage
1. Clone or download the source code of the scraping application from the repository.
2. Navigate to the directory containing the `script.py` file.
3. Open a terminal or command prompt in that directory.

4. Execute the following command to run the scraping application:
```bash
python script.py
```

5. The application will start scraping the provided URLs concurrently. Once scraping is completed, the application will print "Scraping completed." to the console.

## Customization
- You can customize the list of URLs to scrape by modifying the `urls` list in the `scrape.py` file.
- Adjust the maximum number of workers in the thread pool by modifying the `max_workers` parameter in the `scrape_urls()` function in `scrape.py`.

## Logging
- Error logs are written to the `scrap.log` file in the same directory as `scrape.py`. Check this file for any errors encountered during the scraping process.

## Error Handling
- The application handles various types of errors gracefully and logs them for debugging purposes. If any URL fails to be scraped, the application will print a corresponding error message.



