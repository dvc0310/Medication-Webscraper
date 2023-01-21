import pprint
import requests
from bs4 import BeautifulSoup
import time
import re
import pandas as pd
import os
from string import ascii_lowercase
import pathlib

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}
desktop = pathlib.Path.home() / 'Desktop'
combined_path = os.path.join(desktop, "meds.csv")
#def scrape_conditions(Dict):
read_file = pd.read_csv (r'medication_scraper\drug_ratings.txt', delimiter='|')
read_file.to_csv(r"medication_scraper\meds.csv")
#scrape_conditions(Dict)

