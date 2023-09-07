from bs4 import BeautifulSoup
import requests
import unicodedata
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import json


def user_agent():
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    return user_agent


def soup(link, user_agent):
    req = requests.get(link, headers=user_agent)

    soup = BeautifulSoup(req.text, 'html.parser')

    if 'babel' in link:
        return soup.find_all('main', 'main')
    elif 'catalog' in link:
        return soup.find_all('main', 'main-container')
    elif 'worldcat' in link:
        return [item.a['href'] for item in soup.find_all('div', 'tss-1r4yf2c-conditionalMargin MuiBox-root mui-my9yfq')]
    elif 'archive.org' in link:
        return soup.find_all('div', 'col-sm-4 thats-right item-details-archive-info')


def hrefLink(headlink, items):
    for item in items:
        for a in item.select('section.boxy.item-download-options div.format-group a.format-summary.download-pill'):
            tag = removeStrTag('span', a)
            if 'PDF' == tag.text.strip():
                return headlink+tag['href']


def removeStrTag(tag, induk):
    for tags in induk.find_all(tag):
        tags.string = ''
    return induk


def options():
    options = ['all', 'title', 'author', 'subject',
               'isn', 'publisher', 'seriestitle']
    return options


# def linkPdf(librarys):

#     driver = webdriver.Chrome()

#     driver.get(librarys)

#     accept = driver.find_element(
#         By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
#     action = ActionChains(driver)

#     action.click(on_element=accept)
#     action.perform()

#     links = driver.find_element(
#         By.XPATH, '//a[@data-testid="access-free-button"]')

#     href = links.get_attribute('href')
#     driver.quit()

#     if 'archive.org' in href:
#         items = soup(href, user_agent())
#         hrefResult = hrefLink('http://www.archive.org', items)
#         return hrefResult
#     elif 'catalog.hathitrust.org' in href:
#         return ''
#     else:
#         return href


def unique(inList):
    unique_list = []
    [unique_list.append(x) for x in inList if x not in unique_list]
    return unique_list


def forfindall(item, tag, key):
    for nktag in item.find_all(tag, key):
        return nktag


def clearLast(text):
    char = ",./;'[\=-`<:|{(*&^$#@~"
    return text.rstrip(char)


def clean(text):
    cleaned = re.sub(r'\n+', '\n', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned)
    normalized = unicodedata.normalize('NFKD', cleaned_text)
    ascii_text = normalized.encode('ascii', 'ignore').decode('ascii')
    replace_text = ascii_text.replace('\"', "'")
    if replace_text[0] == ' ' and replace_text[-1] == ' ':
        return replace_text[1:-1]
    if replace_text[0] == ' ':
        return replace_text[1:]
    if replace_text[-1] == ' ':
        return replace_text[:-1]
    else:
        return replace_text


def dtddList(item, desc):
    return [clearLast(clean(a.text)) for grid in item.find_all('div', 'grid') for dt in grid.find_all(
            'dt', 'g-col-lg-4 g-col-12') if dt.text == desc for dd in grid.find_all('dd', 'g-col-lg-8 g-col-12') for a in dd.find_all('a')]


def takeResults1(items, page):
    for item in items:
        try:
            links = ['http://catalog.hathitrust.org' + takehref['href'].replace('#viewability', '')
                     if 'http://catalog.hathitrust.org' not in takehref['href']
                     else takehref['href'].replace('#viewability', '')
                     for takehref in item.find_all('a', 'list-group-item list-group-item-action w-sm-50')]
        except:
            links = items

        next_page = [hrp['data-prop-next-href'][-1]
                     for hrp in item.find_all('hathi-results-pagination')]

        if next_page == page-1:
            return unique(links), ''
        elif next_page != page-1:
            return unique(links), next_page


# items = soup('https://catalog.hathitrust.org/Search/Home?lookfor={0}&searchtype={1}&ft=ft&setft=true&page={2}'.format(
#     'title', 'islam', '100'), user_agent())

# takeResults1(items, '100')
