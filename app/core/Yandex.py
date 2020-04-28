# Falla-Yandex
# -*- encoding: utf-8 -*-
# Sanix-darker

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from app.core.Falla import Falla


class Yandex(Falla):
    def __init__(self):
        self.option = Options()
        self.option.headless = True
        self.driver = webdriver.Firefox(options=self.option)

        self.try_it = 0
        self.max_retry = 3
        self.source = "Yandex"
        self.mode = "selenium"
        self.results_box = "//div[@class='content__left']"
        self.each_element = {
            "tag": "li",
            "attr": {"class": "serp-item"}
        }
        self.href = {
            "tag": "a:link",
            "type": "attribute",
            "key": "href",
            "child": {}
        }
        self.title = {
            "tag": "div:organic__url-text",
            "type": "text"
        }
        self.cite = {
            "tag": "div:organic__content-wrapper",
            "child": {
                "tag": "div:text-container",
                "type": "text"
            }
        }

    def search(self, search_text):
        url = "https://yandex.com/search/?text=" + search_text.replace(" ", "+")
        return self.fetch(url)

# y = Yandex()
# print(y.search("un avion"))
