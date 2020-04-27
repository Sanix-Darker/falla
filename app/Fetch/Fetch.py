# Google-fetcher
# -*- encoding: utf-8 -*-
# Sanix-darker

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://www.google.com/search?q=meryl+bitee"

def fetch():

    element = driver.find_element_by_xpath("//div[@id='search']")
    html_content = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_content, 'html.parser')
    
    fetchs = []
    fetchs = soup.findAll("div", {"class": "g"})
    
    results = []
    for elt in fetchs:
        element = {
            "href": elt.find("a")["href"],
            "title": str(elt.find("a").find("h3").getText()),
            "cite": str(elt.find("a").find("cite").getText())
        }
        results.append(element)

    print("[+] results: ", results)

    return results


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)
driver.implicitly_wait(10)  # in seconds

results = fetch()

driver.quit()

# Dump and Save to JSON file (Converter e salvar em um arquivo JSON)
with open('results.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(results, indent=4)
    jp.write(js)

print("[+] Done !")