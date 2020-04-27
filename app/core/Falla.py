# Falla
# -*- encoding: utf-8 -*-
# Sanix-darker

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

class Falla:
    def __init__(self, results_box, each_element, href, title, cite):
        self.results_box = results_box
        self.each_element = each_element
        self.href = href
        self.title = title
        self.cite = cite

    def get_element_from_type(self, to_return, the_filter=None):
        if the_filter["type"] == "text":
            to_return = to_return.getText()
        elif  the_filter["type"] == "attibute":
            to_return = to_return[the_filter["key"]]
        else:
            print("[x] Error, specify a valid type !")

        return to_return

    def parse_entry_point(self, element, the_filter):
    
        to_return = element.find(the_filter["tag"])
        if "type" in the_filter:
            to_return = self.get_element_from_type(to_return, the_filter)
        else:
            if bool(the_filter["child"]): # There are some child
                to_return = to_return.find(the_filter["child"]["tag"])
                to_return = self.get_element_from_type(to_return, the_filter["child"])
            else:
                print("[x] Malformed filter !")

        return ' '.join(str(to_return).split())

    def get_each_elements(self, soup):

        fetchs = []
        if "attr" in self.each_element:
            if self.each_element["attr"] is not None:
                fetchs = soup.findAll(self.each_element["tag"], self.each_element["attr"])
            else:
                fetchs = soup.findAll(self.each_element["tag"])
        else:
            fetchs = soup.findAll(self.each_element["tag"])

        return fetchs

    def fetch(self, url):

        self.driver.get(url)
        self.driver.implicitly_wait(10)  # in seconds

        element = self.driver.find_element_by_xpath(self.results_box)
        html_content = element.get_attribute('outerHTML')

        soup = BeautifulSoup(html_content, 'html.parser')
        
        fetchs = self.get_each_elements(soup)

        results = []
        for elt in fetchs:
            element = {
                "href": self.parse_entry_point(elt, self.href), # elt.find("a")["href"]
                "title": self.parse_entry_point(elt, self.title), # str(elt.find("a").find("h3").getText())
                "cite": self.parse_entry_point(elt, self.cite) # str(elt.find("a").find("cite").getText())
            }
            results.append(element)

        self.driver.quit()

        return json.dumps(results, ensure_ascii=False)
