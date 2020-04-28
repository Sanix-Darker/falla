# Falla-Yahoo
# -*- encoding: utf-8 -*-
# Sanix-darker

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from app.core.Falla import Falla

class Yahoo(Falla):
    def __init__(self):
        # driver parameters
        self.option = Options()
        self.option.headless = True
        self.driver = webdriver.Firefox(options=self.option)

        self.try_it = 0
        self.max_retry = 3
        self.source = "Yahoo"
        self.mode = "selenium"
        self.results_box = "//div[@id='web']"
        self.each_element = {
            "tag": "li"
        }
        self.href = {
            "tag": "a",
            "type": "attribute",
            "key": "href",
            "child": {}
        }
        self.title = {
            "tag": "a",
            "type": "text"
        }
        self.cite = {
            "tag": "div:compText",
            "child": {
                "tag": "p",
                "type": "text"
            }
        }

    def search(self, search_text):
        
        url = "https://search.yahoo.com/search?p="+search_text.replace(" ", "+")
        return self.fetch(url)

# y = Yahoo()
# print(y.search("un avion"))
