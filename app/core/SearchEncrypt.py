# Falla-SearchEncrypt
# -*- encoding: utf-8 -*-
# Sanix-darker

from app.core.Falla import Falla


class SearchEncrypt(Falla):
    def __init__(self):
        self.try_it = 0
        self.max_retry = 3
        self.source = "SearchEncrypt"
        self.mode = "requests"
        self.results_box = "//section[@class='serp__results']"
        self.each_element = {
            "tag": "div",
            "attr": {"class": "web-result"}
        }
        self.href = {
            "tag": "a:web-result__link",
            "type": "attribute",
            "key": "href",
            "child": {}
        }
        self.title = {
            "tag": "a:web-result__link",
            "type": "text",
            "child": {}
        }
        self.cite = {
            "tag": "p:web-result__description",
            "child": {
                "tag": "span",
                "type": "text"
            }
        }

    def search(self, search_text):
        url = "https://www.searchencrypt.com/search/?q=" + search_text.replace(" ", "+")
        return self.fetch(url)

# se = SearchEncrypt()
# print(se.search("un avion"))
