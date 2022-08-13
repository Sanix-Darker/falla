from os import listdir as ls
from app.core import ENGINES
import json


class Bcolors:
    """
    Some colors for the terminal
    """
    AUTRE = '\033[96m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def list_engines():
    """

    """
    print(Bcolors().OKBLUE + "[+] Listing search-Engines" + Bcolors().ENDC)
    for e in ENGINES.keys():
        print("[+] > " + Bcolors().AUTRE + e + Bcolors().ENDC)


def get_results(engine, query, pages):
    """

    """
    f = ENGINES[engine]()

    results = json.loads(f.search(query, pages))
    bcolors = Bcolors()

    for elt in results:
        print("|> " + bcolors.OKBLUE + elt["title"] + bcolors.ENDC)
        print("|- " + bcolors.WARNING + elt["href"] + bcolors.ENDC)
        print("|| " + elt["cite"])
