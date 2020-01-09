# qudaisozi-scraper
Scraper for qudaisozi.com, a Kazakh Bible

Use `./scraper.py` with no arguments to scrape the site. Output in
`./Bible.txt`. Note the capital B! The scraper dumps text into `Bible.txt`
every time it finishes a book, which occurs 66 times (because there are 66
books in the Bible).

`scraper.py` has some options. See `scraper.py --help`.

This scraper makes a best effort attempt at gathering data. If it cannot
scrape a section, book, or chapter, that portion will be omitted and a warning
printed.

## Dependencies
* requests
* beautifulsoup4
* Python 3
