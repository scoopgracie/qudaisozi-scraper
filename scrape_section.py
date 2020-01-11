#!/usr/bin/env python3
#scrape_section.py - qudaisozi scraper - scrape section
import scrape_book
import get_page
def scrape(url):
    '''scrape(url) - scrape section <url> (starting with /) from qudaisozi.com,
return generator of Book objects, or empty list on error'''
    url = 'https://qudaisozi.com{}'.format(url) #URLs come starting with the /
    try:
        page = get_page.get(url)
        links = page.find_all(class_='book') #Get all links to books
        print('got section {}'.format(url))
        for link in links:
            book = scrape_book.scrape(link.a['href'])
            if book is not None:
                yield book
    except Exception as e:
        if type(e) == KeyboardInterrupt:
            print('exiting')
            exit(0)
        print('error on section {}'.format(url))
        return []
