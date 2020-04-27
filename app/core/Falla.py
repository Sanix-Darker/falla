# Falla
# -*- encoding: utf-8 -*-
# Sanix-darker

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import time
from app.settings import *

class Falla:
    def __init__(self, results_box, each_element, href, title, cite):
        self.results_box = results_box
        self.each_element = each_element
        self.href = href
        self.title = title
        self.cite = cite
        self.try_it = 0
        self.max_retry = 4
        self.source = "Falla"
        self.mode = "requests"

    def get_element_from_type(self, to_return, the_filter=None):
        if the_filter["type"] == "text":
            to_return = to_return.getText()
        elif  the_filter["type"] == "attribute":
            try:
                to_return = to_return[the_filter["key"]]
            except Exception as es:
                to_return = ""
        else:
            print("[x] Error, specify a valid type !")

        return to_return

    def get_tag(self, element, tag):
        if ":" in tag:
            return element.find(tag.split(":")[0], {"class": tag.split(":")[1]})
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

    def scrapy_splash_request(self, to_fetch_url):

        json_data = {
            "response_body":False,
            "lua_source":"function main(splash, args)\r\n  assert(splash:go(args.url))\r\n  assert(splash:wait(0.5))\r\n  return {\r\n    html = splash:html(),\r\n    png = splash:png(),\r\n    har = splash:har(),\r\n  }\r\nend",
            "url":to_fetch_url,
            "html5_media":False,
            "save_args":[],
            "viewport":"1024x768",
            "http_method":"GET",
            "resource_timeout":0,
            "render_all":False,
            "png":1,
            "har":1,
            "timeout":90,
            "request_body":False,
            "load_args":{},
            "html":1,
            "images":1,
            "wait":0.7
        }

        url = SPLASH_SCRAP_URL + "/execute"

        r = requests.post(url, json=json_data)

        html_string = json.loads(r.content.decode())["html"]

        return html_string

    def get_html_content(self, url):
        
        if self.mode == "selenium":
            self.driver.get(url)
            self.driver.implicitly_wait(10)  # in seconds

            element = self.driver.find_element_by_xpath(self.results_box)
            html_content = element.get_attribute('outerHTML')
        elif self.mode == "splash_scrap":
            html_content = self.scrapy_splash_request(url)

        elif self.mode == "requests":
            r = requests.get(url, headers={"Upgrade-Insecure-Requests": "1", 
                                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
                                            "Sec-Fetch-Dest": "document",
                                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            })
            html_content = r.content.decode()
        
        # print("html_content: ", html_content)

        return html_content

    def fetch(self, url):

        html_content = self.get_html_content(url)
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        fetchs = self.get_each_elements(soup)

        results = []
        # print("fetchs: ", fetchs)
        # print("self.parse_entry_point(elt, self.href): ", self.parse_entry_point(fetchs[0], self.href))
        # print("self.parse_entry_point(elt, self.title): ", self.parse_entry_point(fetchs[0], self.title))
        # print("self.parse_entry_point(elt, self.cite): ", self.parse_entry_point(fetchs[0], self.cite))
        for elt in fetchs:
            element = {
                "source": self.source,
                "href": self.parse_entry_point(elt, self.href), # elt.find("a")["href"]
                "title": self.parse_entry_point(elt, self.title), # str(elt.find("a").find("h3").getText())
                "cite": self.parse_entry_point(elt, self.cite) # str(elt.find("a").find("cite").getText())
            }
            results.append(element)

        if len(results) == 0 and self.try_it < self.max_retry:
            self.try_it += 1
            time.sleep(0.5)
            print("[+] try: ", self.try_it)
            self.fetch(url)

        if self.mode == "selenium":
            self.driver.quit()

        return json.dumps(results, ensure_ascii=False)
