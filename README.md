# Medication Scraper

This project is a Python-based web scraper designed to collect information about various drugs from the website `drugs.com`. The collected data includes drug name, classes, rating, number of reviews, and usage. The program then saves this data to a CSV file for further analysis.

## Dependencies

The script relies on several Python libraries. You will need to have the following installed:

- `requests`
- `BeautifulSoup4`
- `time`
- `re`
- `random`
- `pandas`
- `drugScraper` (a custom module used in this script)

You can install the required libraries using pip:

```shell
pip install requests beautifulsoup4 pandas
```

Note: The `drugScraper` module is a custom module used in this script. Please ensure you have it in your PYTHONPATH or in the same directory as this script. 

## How to Run

Ensure all the dependencies are installed and you have the `drugScraper` module in the correct location. 

The output of the script will be written to the `drug_ratings.txt` file within the `medication_scraper` directory. This file is then read by the script and converted to a CSV file, `meds.csv`, for easier data manipulation. Ensure the `medication_scraper` directory exists before running the script.

Once all the setup is complete, run the Python script as you would any other:

```shell
python drug_scraper.py
```

You can then access the scraped data in the `meds.csv` file.

## Important Note

Please be aware of the terms of service on `drugs.com` regarding web scraping. Always ensure you are respectful and considerate when running web scraping tools to prevent overloading the server. This webscraper was designed to scrape slower than it could to prevent overloading the website.

