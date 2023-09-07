from hathitrust import takeLink, crawling
import json

if __name__ == '__main__':

    print('OPTION => ftaf = Full Text & All Fields, all, title, author, subject, isn, publisher, seriestitlee')
    option = input('Masukkan Opsi : ')
    keyword = input('Masukkan Keyword : ')

    links = takeLink(option, keyword)

    count = 1
    results = []
    for url in links:
        results.append(crawling(url=url))
        datas = json.dumps(results, indent=4)

        try:
            with open(f'Result/hathitrust{option}{keyword}.json', 'w') as file:
                file.write(datas)
        except:
            with open(f'Result/hathitrust{option}{keyword}.json', 'r+') as file:
                file.write(datas)

        print('Data {0}-Berhasil!'.format(count))
        count += 1
