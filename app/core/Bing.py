# Falla-Bing
# -*- encoding: utf-8 -*-
# Sanix-darker

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from app.core.Falla import Falla

class Bing(Falla):
    def __init__(self):
        # driver parameters
        self.mode = "splash_scrap"

        self.results_box = "//ol[@id='b_results']"
        self.each_element = {
            "tag": "li",
            "attr": {"class": "b_algo"}
        }
        self.href = {
            "tag": "a",
            "type": "attibute",
            "key": "href",
            "child": {}
        }
        self.title = {
            "tag": "h2",
            "type": "text",
            "child": {}
        }
        self.cite = { 
            "tag": "div:b_caption",
            "child": {
                "tag": "p",
                "type": "text"
            }
        }

    def search(self, search_text):
        
        url = "https://www.bing.com/search?q="+search_text.replace(" ", "+")
        return self.fetch(url)

b = Bing()
print(b.search("un avion"))
