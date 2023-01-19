import pprint
import requests
from bs4 import BeautifulSoup
import time
import re
import pandas as pd
from string import ascii_lowercase

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}
def scrape_drugs(site, dictionary):
    
    page = requests.get(site)
    soup = BeautifulSoup(page.content, "html.parser")
    
    drugList = soup.findAll("ul", class_="ddc-list-column-2")
    
    for drug in drugList:
        for li in(drug.find_all('a')):
            dictionary[li.contents[0]] = {'name': li.contents[0], 'link': li.get('href')}
        

def scrapelink(Dict):
    baseURL = "https://www.drugs.com/alpha/"
    siteList = []
    for c in ascii_lowercase:
        siteList.append(baseURL + c + ".html")

    siteList.append(baseURL + "0-9.html")

    for site in siteList:
        (scrape_drugs(site, Dict))
        


    
