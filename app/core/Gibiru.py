# Falla-Gibiru
# -*- encoding: utf-8 -*-
# Sanix-darker

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from app.core.Falla import Falla

class Gibiru(Falla):
    def __init__(self):
        self.source = "Gibiru"
        self.mode = "splash_scrap"
        self.try_it = 0
        self.max_retry = 3
        self.results_box = "//div[@class='gsc-resultsRoot']"
        self.each_element = {
            "tag": "div",
            "attr": {"class": "gs-webResult"}
        }
        self.href = {
            "tag": "a:gs-title",
            "type": "attribute",
            "key": "data-ctorig",
            "child": {}
        }
        self.title = {
            "tag": "a:gs-title",
            "type": "text",
            "child": {}
        }
        self.cite = {
            "tag": "div:gs-snippet",
            "type": "text",
            "child": {}
        }

    def search(self, search_text):
        
        url = "https://gibiru.com/results.html?q="+search_text.replace(" ", "+")
        return self.fetch(url)

# gi = Gibiru()
# print(gi.search("un avion"))
