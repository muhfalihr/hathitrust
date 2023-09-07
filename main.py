from hathitrust import takeLink, crawling
import json

if __name__ == '__main__':

    print('OPTION => ftaf = Full Text & All Fields, all, title, author, subject, isn, publisher, seriestitlee')
    option = input('Masukkan Opsi : ')
    keyword = input('Masukkan Keyword : ')
    page = input('Masukkan page : ')

    try:
        links, pages = takeLink(option, keyword, page)
    except TypeError:
        pages = ''

    status = 400 if pages == "" else 200

    results = []
    fix_datas = {
        'status': status,
        'data': results,
        'next_page': pages
    }
    try:
        count = 1
        for url in links:
            results.append(crawling(url=url))
            datas = json.dumps(fix_datas, indent=4)

            try:
                with open(f'Result/hathitrust{option}{keyword}.json', 'w') as file:
                    file.write(datas)
            except:
                with open(f'Result/hathitrust{option}{keyword}.json', 'r+') as file:
                    file.write(datas)

            print('Data {0}-Berhasil!'.format(count))
            count += 1
    except NameError:
        datas = json.dumps(fix_datas, indent=4)

        try:
            with open(f'Result/hathitrust{option}{keyword}.json', 'w') as file:
                file.write(datas)
        except:
            with open(f'Result/hathitrust{option}{keyword}.json', 'r+') as file:
                file.write(datas)
        print('Data {0}-Berhasil!'.format(count))
