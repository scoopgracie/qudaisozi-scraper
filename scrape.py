#!/usr/bin/env python3
#scrape.py - qudaisozi.com scraper - main program
import scrape_section

urls = [
    '/tawrat/',
    '/tarixtik-kitaptar',
    '/naqil-sozder',
    '/zabuуr',
    '/paygambarlardeng-jazbalare',
    '/injil'
]

Bible = []
for url in urls:
    books = scrape_section.scrape(url)
    for book in books:
        Bible.append(book)

Bible_text = ''

for book in Bible:
    if book is not None:
        for chapter in book.chapters:
            if chapter is not None:
                Bible_text += str(book.name) + ' ' + str(chapter.number) + '\n'
                for verse in chapter.verses:
                    Bible_text += str(verse.number) + ' ' + verse.text + '\n'
                Bible_text += '\n'

text = Bible_text.strip() + '\n'
with open('Bible.txt', 'w+') as f:
    f.write(text)
