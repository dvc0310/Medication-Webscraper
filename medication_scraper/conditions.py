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

#def scrape_conditions(Dict):
site = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z'
page = requests.get(site)
soup = BeautifulSoup(page.content, "html.parser")
conditions_list = soup.find_all('div', class_ = 'wrapper')
#.find('div').find('div', class_='row')
rows = conditions_list[4].contents[1].contents[3]
i = 0
for condition in rows:
    if condition != '\n' and i > 1 and not condition.has_attr('id'):
        lst = condition.contents[1]
        for c in lst:
            if c != '\n':
                print(c.text.strip())
        
    i = i + 1
#Dict = {}
#scrape_conditions(Dict)

