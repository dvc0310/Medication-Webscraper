import pprint
import requests
from bs4 import BeautifulSoup
import time
import re
import pandas as pd
from string import ascii_lowercase
import drugScraper as ds


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}
with open('WebMDscraper/readme2.txt', 'w+', encoding="utf-8") as f:
    Dict = {}
    print('Drug Name | Drug Classes | Rating | Number of Reviews', file=f)
    ds.scrapelink(Dict)
    for k, v in Dict.items():
        page = requests.get('http://drugs.com/' + v['link'])
        soup = BeautifulSoup(page.content, "html.parser")
        target_subtitle = soup.find_all("p", class_='drug-subtitle', recursive=True)
        if len(target_subtitle) > 0:
            drug_class_list = target_subtitle[0].find_all('a', href=True)
        else:
            continue
        dc_lst = []
        for drug_class in drug_class_list:
            for x in drug_class: 
                if x != '\n':
                    if drug_class.has_attr('href') and 'drug-class' in drug_class['href']:
                        dc_lst.append(x)
                        
       
        
        v['drug class list'] = dc_lst            
            
        rating_subtitle = soup.find_all("div", class_='ddc-rating-summary', recursive=True)    
        
   
        #, v['uses list'], ' |' 

        try:
            rating = rating_subtitle[0].find('a').string
            rating = re.sub(',', '', rating)
            rating = re.findall('\d+', rating)[0]
            print(v['name'] + ' |', v['drug class list'], ' |' ,rating_subtitle[0].find('b').string,' |' , rating, file=f)
            print(v['name'] + ' |', v['drug class list'], ' |' ,rating_subtitle[0].find('b').string, ' |' , rating,)
        except:
            print(v['name'] + ' |', v['drug class list'], ' | N/A', ' | N/A', file=f)
            print(v['name'] + ' |', v['drug class list'], ' | N/A', ' | N/A')
 
        
        
        
""" target_uses = soup.find_all('h2',id='uses')
        uses_lst = []
        for use_tag in target_uses:
            for item in use_tag.next_siblings:
                if item.name=="h2": 
                    break
                try:
                    if item != '\n':
                        for c in item:
                            if c.name == 'a' and 'cg' in c.attrs['href']:
                                uses_lst.append(c.string)
                            elif c.name == 'a' and 'health-guide' in c.attrs['href']:
                                uses_lst.append(c.string)             
                except:
                    continue
                
        v['uses list'] = uses_lst """        
       