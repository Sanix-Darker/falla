from os import listdir as ls
from app.core import *
import json


class Bcolors:
    """[summary]
    """
    AUTRE = '\033[96m'  # rose
    HEADER = '\033[95m'  # rose
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'  # jaune
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def list_engines():
    print(Bcolors().OKBLUE + "[+] Listing search-Engines" + Bcolors().ENDC)
    engines = [elt.replace(".py", "").lower() for elt in ls("./app/core/") if
               ".py" in elt and "__" not in elt and "falla" not in elt]
    for e in engines:
        print("[+] > " + Bcolors().AUTRE + e + Bcolors().ENDC)


def get_results(engine, query):
    if engine == "aol" or engine == "al":
        f = Aol()
    elif engine == "ask" or engine == "ak":
        f = Ask()
    elif engine == "bing" or engine == "b":
        f = Bing()
    elif engine == "dogpile" or engine == "dp":
        f = DogPile()
    elif engine == "duckduckgo" or engine == "dd":
        f = DuckDuckGo()
    elif engine == "gibiru" or engine == "gu":
        f = Gibiru()
    elif engine == "mojeek" or engine == "m":
        f = Mojeek()
    elif engine == "qwant" or engine == "q":
        f = Qwant()
    elif engine == "searchencrypt" or engine == "se":
        f = SearchEncrypt()
    elif engine == "startpage" or engine == "sp":
        f = StartPage()
    elif engine == "yahoo" or engine == "y":
        f = Yahoo()
    elif engine == "google" or engine == "g":
        f = Google()
    else:
        f = Google()

    results = json.loads(f.search(query))
    bcolors = Bcolors()

    for elt in results:
        print("|> " + bcolors.OKBLUE + elt["title"] + bcolors.ENDC)
        print("|- " + bcolors.WARNING + elt["href"] + bcolors.ENDC)
        print("|| " + elt["cite"])
        print("")
