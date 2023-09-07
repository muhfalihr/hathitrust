from utility import user_agent, options, soup, clearLast, clean, takeResults1
from tools import Book


def takeLink(option='', keyword='', page='1'):
    '''option => ftaf = Full Text & All Fields, all, title, author, subject, isn, publisher, seriestitle'''
    try:
        if option == 'ftaf':
            link = f'https://babel.hathitrust.org/cgi/ls?q1={keyword}&field1=ocr&a=srchls&ft=ft&lmt=ft'
        elif option in options():
            link = 'https://catalog.hathitrust.org/Search/Home?lookfor={0}&searchtype={1}&ft=ft&setft=true&page={2}'.format(
                keyword, option, page)

        items = soup(link, user_agent())

        links, pages = takeResults1(items, page)

        return links, pages

    except:
        return None


def crawling(url):

    items = soup(url, user_agent())

    for item in items:
        title = clearLast(clean(item.find(
            'div', 'article-heading d-flex gap-3').h1.text))

        grids1 = [clean(grid.text).lower().replace(' ', '_')
                  for grid in item.find_all('dt', 'g-col-lg-4 g-col-12')]

        grids = [clearLast(clean(grid.text))
                 for grid in item.find_all('dd', 'g-col-lg-8 g-col-12')]

        # librarys = [a_tags['href'] for a in item.find_all(
        #     'dd', 'g-col-lg-8 g-col-12') for a_tags in a.find_all('a') if 'Find in a library' in a_tags.text]

        tools = Book(grids1, grids, item)

        results = {
            'title': title,
            'description': {
                'main_author': tools.author(),
                'related_names': tools.relnam(),
                'language': tools.language(),
                'published': tools.publish(),
                'subjects': tools.subject(),
                'summary': tools.summaryTeks(),
                'note': tools.noteTeks(),
                'physical_description': tools.physdesc(),
                'download_pdf': ''
            }
        }
        return results
