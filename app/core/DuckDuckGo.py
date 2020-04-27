# Falla-DuckDuckGo
# -*- encoding: utf-8 -*-
# Sanix-darker

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from app.core.Falla import Falla

class DuckDuckGo(Falla):
    def __init__(self):
        # driver parameters
        self.option = Options()
        self.option.headless = True
        self.driver = webdriver.Firefox(options=self.option)

        self.use_selenium = True
        self.results_box = "//div[@id='links']"
        self.each_element = {
            "tag": "div",
            "attr": {"class": "result__body"}
        }
        self.href = {
            "tag": "a:result__a",
            "type": "attibute",
            "key": "href",
            "child": {}
        }
        self.title = {
            "tag": "a:result__a",
            "type": "text",
            "child": {}
        }
        self.cite = { 
            "tag": "div:result__snippet",
            "type": "text",
            "child": {}
        }

    def search(self, search_text):
        
        url = "https://duckduckgo.com/?q="+search_text.replace(" ", "+")
        return self.fetch(url)

d = DuckDuckGo()
print(d.search("un avion"))
