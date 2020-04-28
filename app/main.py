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
    prs = argparse.ArgumentParser()
    prs.add_argument('-e', '--engine', help='The search engine', type=str, default="google")
    prs.add_argument('-q', '--query', help='The query text', type=str)
    prs = prs.parse_args()

    print("[+] Falla [the search-engine-scraper]")
    if prs.engine != None and prs.query != None :
        get_results(engine=prs.engine.lower(), query=prs.query.lower())
    else:
        list_engines()
