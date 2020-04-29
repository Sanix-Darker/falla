# main-script
# -*- encoding: utf-8 -*-
#  _____ _    _     _        _    
# |  ___/ \  | |   | |      / \   
# | |_ / _ \ | |   | |     / _ \  
# |  _/ ___ \| |___| |___ / ___ \ 
# |_|/_/   \_\_____|_____/_/   \_\
#
# By Sanix-darker
__version__ = 0.1
__author__ = "Sanix-darker"

import argparse
from app.utils import *

if __name__ == "__main__":
    # Initialize the arguments
    # python3 -m app.main # Search-Engine list
    # python3 -m app.main -e aol -q "sanix darker"
    #
    # python3 -m app.main -e google -q "sanix darker" -p "&start=10"
    prs = argparse.ArgumentParser()
    prs.add_argument('-e', '--engine', help='The search engine', type=str, default="google")
    prs.add_argument('-q', '--query', help='The query text', type=str)
    prs.add_argument('-p', '--page', help='Number of pages to fetch', type=str, default="")
    prs = prs.parse_args()

    print("[+] Falla [the search-engine-scraper]")
    if prs.engine is not None and prs.query is not None:
        get_results(engine=prs.engine.lower(), query=prs.query.lower(), pages=prs.page)
    else:
        list_engines()
