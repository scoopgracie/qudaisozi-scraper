#!/usr/bin/env python3
#scrape.py - qudaisozi.com scraper - main program
import scrape_section
import argparse

parser = argparse.ArgumentParser(description='Scrape qudaisozi.com')
#Let the user pick which part
parser.add_argument('-t', '--testament', help='which testament(s) to scrape (default `all`)', choices=['old', 'new', 'all'])
#Let the user pick the output file
parser.add_argument('-o', '--output-file', help='change the output file (default `Bible.txt`)')
args = parser.parse_args()
old_testament = [
    '/tawrat/',
    '/tarixtik-kitaptar',
    '/naqil-sozder',
    '/zabuуr',
    '/paygambarlardeng-jazbalare',
]
new_testament = [
    '/injil'
]
if args.testament == 'old':
    urls = old_testament
elif args.testament == 'new':
    urls = new_testament
else: #Scrape the whole Bible
    urls = old_testament + new_testament

file_name = args.output_file or 'Bible.txt' #Default to Bible.txt

with open(file_name, 'w+') as f:
    #Create or empty the file)
    f.write('')

sections = [ scrape_section.scrape(url) for url in urls ]

for section in sections:
    for book in section:
        chapters = [chapter for chapter in book.chapters if chapter is not None]
        #Ignore errors
        for chapter in chapters:
            Bible_text = '{} {}\n'.format(book.name, chapter.number) #Chapter header
            for verse in chapter.verses:
                Bible_text += '{} {}\n'.format(verse.number, verse.text) #Verse format
            Bible_text += '\n' #Put a blank line between chapters
            with open(file_name, 'a+') as f:
                f.write(Bible_text)
                print('wrote chapter {} {} to {}'.format(book.name, chapter.number, file_name))
