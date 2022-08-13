# main-script
# -*- encoding: utf-8 -*-
# Falla
# By Sanix-darker

__version__ = 0.1
__author__ = 'Sanix-darker'

import argparse
from app.utils import get_results, list_engines

# Initialize the arguments
# python3 -m app.main # Search-Engine list
# python3 -m app.main -e aol -q "sanix darker"
#
# python3 -m app.main -e google -q "sanix darker" -p "&start=10"
if __name__ == "__main__":
    prs = argparse.ArgumentParser()
    prs.add_argument(
        '-e',
        '--engine',
        help='The search engine',
        type=str,
        default="google"
    )
    prs.add_argument(
        '-q',
        '--query',
        help='The query text',
        type=str
    )
    prs.add_argument(
        '-p',
        '--page',
        help='Number of pages to fetch',
        type=str,
        default=""
    )
    prs = prs.parse_args()

    print('[+] Falla [the search-engine-scraper]')
    if prs.engine and prs.query:
        engine = prs.engine.lower()
        query = prs.query.lower()
        get_results(
            engine=engine,
            query=query,
            pages=prs.page
        )
    else:
        list_engines()
