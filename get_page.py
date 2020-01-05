#!/usr/bin/env python3
#get_page.py - qudaisozi.com scraper - get a page and parse it
import requests
from bs4 import BeautifulSoup
class NotFoundError(Exception):
    pass

cache = {}
def get(url):
    if url in cache.keys():
        print('got ' + url + ' from cache')
        return cache[url]
    else:
        request = requests.get(url)
        if request.status_code == 200:
            soup = BeautifulSoup(request.text, features='lxml')
            print('got ' + url)
            cache[url] = soup
            return soup
        else:
            raise NotFoundError
