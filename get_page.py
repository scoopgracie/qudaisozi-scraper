#!/usr/bin/env python3
#get_page.py - qudaisozi.com scraper - get a page and parse it
import requests
from bs4 import BeautifulSoup
class NotFoundError(Exception):
    '''Raised when a page does not return 200'''
    pass

cache = {}
def get(url):
    '''get(url) - Get page url, return BeautifulSoup object on 200; raise
NotFoundError otherwise'''
    if url in cache.keys():
        response = cache[url]
        del cache[url] #Only use a cached page once
        return response #Get cached page if it exists
    else:
        request = requests.get(url)
        if request.status_code == 200:
            soup = BeautifulSoup(request.text, features='lxml')
            if url.endswith('/1'):
                cache[url] = soup #Cache the page
            return soup
        else:
            raise NotFoundError
