# Falla-Google
# -*- encoding: utf-8 -*-
# Sanix-darker

import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from app.core.Falla import Falla


class Google(Falla):
    def __init__(self):
        self.option = Options()
        self.option.headless = True
        self.driver = webdriver.Firefox(options=self.option)

        self.try_it = 0
        self.max_retry = 3
        self.source = "Google"
        self.mode = "selenium"
        self.results_box = "//div[@id='search']"
        self.each_element = {
            "tag": "div",
            "attr": {"class": "g"}
        }
        self.href = {
            "tag": "a",
            "type": "attribute",
            "key": "href",
            "child": {}
        }
        self.title = {
            "tag": "a",
            "child": {
                "tag": "h3",
                "type": "text"
            }
        }
        self.cite = {
            "tag": "a",
            "child": {
                "tag": "cite",
                "type": "text"
            }
        }

    def search(self, search_text, pages=""):

        base_url = "https://www.google.com/search?q=" + search_text.replace(" ", "+") + pages
        print("[+] Searching results for '" + base_url.split("=")[1].replace("+", " ") +
              "' on '" + self.source + "' :\n")

        # results = json.loads(self.fetch(base_url))
        #
        # if pages > 1:
        #     for nb_page in range(pages):
        #         url = base_url + "&start=" + str(nb_page + 1) + "0"
        #         time.sleep(1)
        #         results = results + self.fetch(url)
        #
        # results = json.dumps(results)

        return self.fetch(base_url)


# g = Google()
# print(g.search("un avion"))
