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
        self.use_selenium = True

    def get_element_from_type(self, to_return, the_filter=None):
        if the_filter["type"] == "text":
            to_return = to_return.getText()
        elif  the_filter["type"] == "attibute":
            to_return = to_return[the_filter["key"]]
        else:
            print("[x] Error, specify a valid type !")

        return to_return

    def get_tag(self, element, tag):
        if ":" in tag:
            return element.find(
                tag.split(":")[0],
                {"class": tag.split(":")[1]}
            )
        else:
            return element.find(tag)

    def parse_entry_point(self, element, the_filter):
    
        to_return = self.get_tag(element, the_filter["tag"])

        if "type" in the_filter:
            to_return = self.get_element_from_type(to_return, the_filter)
        else:
            if bool(the_filter["child"]): # There are some child
                to_return = self.get_tag(to_return, the_filter["child"]["tag"])

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

    def get_html_content(self, url):
        
        if self.use_selenium is not None:
            self.driver.get(url)
            self.driver.implicitly_wait(10)  # in seconds

            element = self.driver.find_element_by_xpath(self.results_box)
            html_content = element.get_attribute('outerHTML')
        else:
            r = requests.get(url, headers={"Upgrade-Insecure-Requests": "1", 
                                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
                                            "Sec-Fetch-Dest": "document",
                                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            })
            html_content = r.content.decode()
            
        return html_content

    def fetch(self, url):

        html_content = self.get_html_content(url)
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        fetchs = self.get_each_elements(soup)

        results = []
        # print("self.parse_entry_point(elt, self.cite): ", self.parse_entry_point(fetchs[0], self.cite))
        for elt in fetchs:
            element = {
                "href": self.parse_entry_point(elt, self.href), # elt.find("a")["href"]
                "title": self.parse_entry_point(elt, self.title), # str(elt.find("a").find("h3").getText())
                "cite": self.parse_entry_point(elt, self.cite) # str(elt.find("a").find("cite").getText())
            }
            results.append(element)

        self.driver.quit()

        return json.dumps(results, ensure_ascii=False)
