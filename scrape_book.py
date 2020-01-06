import classes
import get_page
import scrape_chapter
def scrape(url):
    try:
        page = get_page.get('https://qudaisozi.com' + url)
        dropdowns = page.find_all(class_='dropdown')
        chapter_urls = []
        for dropdown in dropdowns:
            chapters = dropdown.find_all('a')
            for chapter in chapters:
                if not chapter['href'] in chapter_urls:
                    chapter_urls.append(chapter['href'])
    
        book_name = page.find('h1', class_='zhenzhu-da').string[1:][:-1]

        return classes.Book(book_name, [scrape_chapter.scrape(chapter) for chapter in chapter_urls])
#Comment the previous line and uncomment the next one in testing, it will speed it up but only get two chapters per book
#        return classes.Book(book_name, [scrape_chapter.scrape(chapter_urls[0]), scrape_chapter.scrape(chapter_urls[1])])
    except:
        print('error on book {}'.format(url))
        return None
