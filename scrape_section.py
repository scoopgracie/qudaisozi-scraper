#!/usr/bin/env python3
#scrape_section.py - qudaisozi scraper - scrape section
import scrape_book
import get_page
def scrape(url):
    try:
        page = get_page.get('https://qudaisozi.com' + url)
        books = []
        links = page.find_all(class_='book')
        for raw_link in links:
            link = raw_link.a['href']
            books.append(scrape_book.scrape(link))

        return books
    except:
        return []
