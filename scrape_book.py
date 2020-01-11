import classes
import get_page
import scrape_chapter
def scrape(url):
    url = 'https://qudaisozi.com{}'.format(url) 
    try:
        page = get_page.get(url)
        dropdowns = page.find_all(class_='dropdown') #Chapters come in dropdowns
        chapter_urls = []
        for dropdown in dropdowns:
            chapters = dropdown.find_all('a')
            for chapter in chapters:
                if not chapter['href'] in chapter_urls: #Weed out duplicates
                    chapter_urls.append(chapter['href'])
    
        book_name = page.find('h1', class_='zhenzhu-da').string[1:][:-1] #Get the book name and remove the quotes
        chapters = [scrape_chapter.scrape(chapter) for chapter in chapter_urls]
        print('got book {} ({})'.format(url, book_name))
        return classes.Book(book_name, [chapter for chapter in chapter_urls if chapter is not None])
#Comment the previous line and uncomment the next one in testing, it will speed it up but only get two chapters per book
#        return classes.Book(book_name, [scrape_chapter.scrape(chapter_urls[0]), scrape_chapter.scrape(chapter_urls[1])])
    except Exception as e:
        if type(e) == KeyboardInterrupt:
            print('exiting')
            exit(0)
        print('error on book {}'.format(url))
        return None
