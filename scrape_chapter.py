import classes
import get_page
def scrape(url):
    try:
        page = get_page.get('https://qudaisozi.com' + url)
        verse_sections = page.find_all(class_='ersa-0')
        verses = []
        for verse_section in verse_sections:
            for element in verse_section.children:
                try:
                    verse_num = int(element.string)
                except:
                    try:
                        if verses[len(verses)-1].number == verse_num:
                            verses[len(verses)-1].text += element.string
                        else:
                            verses.append(classes.Verse(verse_num, element.string))
                    except Exception:
                        verses.append(classes.Verse(verse_num, element.string))

        return classes.Chapter(int(page.h2.string), verses)
    except Exception:
        print('error on chapter {}'.format(url))
        return None
