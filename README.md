# Medication Webscraper

This project is a Python-based web scraper designed to collect information about various drugs from the website `drugs.com`. The collected data includes drug name, classes, rating, number of reviews, and usage.

## Dependencies

The script relies on several Python libraries. You will need to have the following installed:

- `requests`
- `BeautifulSoup4`
- `time`
- `re`
- `random`
- `drugScraper` (a custom module used in this script)

You can install the required libraries using pip:

```shell
pip install requests beautifulsoup4
```

Note: The `drugScraper` module is a custom module used in this script. Please ensure you have it in your PYTHONPATH or in the same directory as this script. 

## How to Run

Ensure all the dependencies are installed and you have the `drugScraper` module in the correct location. 

The output of the script will be written to the `drug_ratings.txt` file within the `medication_scraper` directory. Ensure this directory exists before running the script.

Once all the setup is complete, run the Python script as you would any other:

```shell
python drug_scraper.py
```

## Important Note

Please be aware of the terms of service on `drugs.com` regarding web scraping. Always ensure you are respectful and considerate when running web scraping tools to prevent overloading the server.

---

Make sure to place this README in your project's root directory, typically named as `README.md`. If you want to display formatted text, I suggest using Markdown language.
