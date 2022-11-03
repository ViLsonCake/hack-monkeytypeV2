import requests
from bs4 import BeautifulSoup
import lxml


def main():
    scripe()


def request():
    url = 'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset=32'
    req = requests.get(url)

    return req.text


def save():
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(request())


def open_file():
    with open('index.html', encoding='utf-8') as file:
        result = file.read()

    return result


def scripe():
    soup = BeautifulSoup(open_file(), 'lxml')
    list_href = []

    result = soup.find_all('div', class_="col-xs-4 col-sm-3 col-md-2 bt-slide")

    for i in result:
        i = i.find('a')

        list_href.append(i.get('href'))

    for i in list_href:
        print(f'{i}\n')


if __name__ == '__main__':
    main()