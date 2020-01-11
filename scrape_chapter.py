import classes
import get_page
def scrape(url):
    '''scrape(url) - scrape chapter <url> (starting with /) from qudaisozi.com,
return Scrape object, or None on error'''
    url = 'https://qudaisozi.com{}'.format(url) 
    try:
        page = get_page.get(url)
        verse_sections = page.find_all(class_='ersa-0') #The verses come spread throughout a bunch of these
        verses = []
        for verse_section in verse_sections:
            for element in verse_section.children:
                try:
                    verse_num = int(element.string) #Try to get the verse number
                except: #If that fails, it's text
                    try:
                        if verses[len(verses)-1].number == verse_num: #If we're on a continuation of the previous verse (i.e. verse number has not changed),
                            verses[len(verses)-1].text += element.string #Append to the last verse
                        else: #Otherwise,
                            verses.append(classes.Verse(verse_num, element.string)) #Add a new verse
                    except Exception:
                        verses.append(classes.Verse(verse_num, element.string)) #If that errors, we're on the first verse. Just append.

        print('got chapter {}'.format(url))
        return classes.Chapter(int(page.h2.string), verses) #page.h2.string is the chapter number
    except Exception as e:
        if type(e) == KeyboardInterrupt:
            print('exiting')
            exit(0)
        print('error on chapter {}'.format(url))
        return None
