#!/usr/bin/env python3
#get_page.py - qudaisozi.com scraper - get a page and parse it
import requests
from bs4 import BeautifulSoup
class NotFoundError(Exception):
    pass

cache = {}
def get(url):
    if url in cache.keys():
        return cache[url] #Get cached page if it exists
    else:
        request = requests.get(url)
        if request.status_code == 200:
            soup = BeautifulSoup(request.text, features='lxml')
            cache[url] = soup #Cache the page
            return soup
        else:
            raise NotFoundError
