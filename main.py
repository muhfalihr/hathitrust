from hathitrust import takeLink, saveData1, saveData2
import json

if __name__ == '__main__':

    print('OPTION => ftaf = Full Text & All Fields, all, title, author, subject, isn, publisher, seriestitlee')
    option = input('Masukkan Opsi : ')
    keyword = input('Masukkan Keyword : ')
    page = input('Masukkan page : ')

    try:
        links, next_pages = takeLink(page, option, keyword)
        saveData1(links, next_pages, option, keyword)
    except ValueError:
        saveData2(option, keyword)
