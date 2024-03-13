# Project Documentation

## Overview
This project comprises several Python scripts designed to gather, process, and analyze data from various sources. It primarily focuses on extracting details about restaurants, grocery stores, and construction services, highlighting Latino and Hispanic businesses within the Washington DC area and the DMV (DC, Maryland, Virginia). These scripts utilize the Google Places API for data collection and pandas for data manipulation and storage. Moreover, the project incorporates functionality to scrape social media links and email addresses from business websites, enriching the dataset with crucial contact information.

## Files Description

### `open_excel.py`
- Demonstrates basic functionality for loading an Excel file using pandas.
- Reads `restaurants.xlsx`, presumably containing restaurant data, and prints the content.

### `instagram.py`
- Augments the dataset with Instagram links.
- Loads an Excel file, iterates through website URLs in the dataset, and uses BeautifulSoup to find Instagram links on each website.
- The enhanced dataset is then saved back into an Excel file.

### `groceries.py`
- Fetches information about Latino grocery stores in the Washington DC area and the DMV using the Google Places API.
- Compiles a list of places, including names, addresses, phone numbers, and websites, then saves this data to an Excel file.

### `fintechapi.py`
- Similar to `groceries.py`, it uses the Google Places API to search for Latino restaurants in the Washington DC area and the DMV.
- Saves the gathered data, including details about each restaurant, to an Excel file named `restaurants.xlsx`.

### `email_scrape.py`
- Enriches the dataset with email addresses by scraping websites listed in `restaurants.xlsx`.
- Utilizes regular expressions to identify and extract email addresses from the HTML content of each website.
- Adds the results to the dataset and saves it to a new Excel file.

### `constructions.py`
- Gathers data on Latino and Hispanic construction services using the Google Places API.
- Fetches essential service details like names, addresses, phone numbers, and websites, saving the information to `constructions.xlsx`.

## Dependencies
- pandas
- BeautifulSoup4
- requests

## Setup and Execution
1. Ensure Python is installed on your system.
2. Install the required dependencies:
   ```sh
   pip install pandas beautifulsoup4 requests
