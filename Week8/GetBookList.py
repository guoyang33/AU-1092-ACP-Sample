# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import requests
import time
import csv

URL = 'https://search.books.com.tw/search/query/key/{0}/cat/all'

def generate_search_url(url, keywd):
    return url.format(keywd)

def get_resource(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64: x64) ApplWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    # return requests.get(url, headers=headers, verify=False)
    return requests.get(url, headers=headers)

def parse_html(r):
    if r.status_code == requests.codes.ok:
        return BeautifulSoup(r.text, 'lxml')
    else:
        print('HTTP requests error!!')

def web_scraping_bot(url):
    booklist = []
    print('...')
    soup = parse_html(get_resource(url))
    for book in soup.find('table', id='itemlist_table').find_all('tbody'):
        book_title = book.find('h4').text.replace('\n', '').replace('\t', '')
        author_list = book.find('ul', class_='list-date').find_all('a')
        book_author = ''
        for author in author_list:
            if author.text == author_list[-1].text:
                book_author = book_author + author.text.replace('\n', '').replace('\t', '')
            else:
                book_author = book_author + author.text.replace('\n', '').replace('\t', '') + ', '
        price_list = book.find('ul', class_='list-nav').find_all('strong')
        if len(price_list) > 1:
            book_price = int(price_list[1].text)
        else:
            book_price = int(price_list[0].text)
        booklist.append({
            'title': book_title,
            'author': book_author,
            'price': book_price
        })

        # print(book_price)
        # print(book_author)
        # print(book.text.replace('\n', '').replace('\t', ''))
    return booklist

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = generate_search_url(URL, sys.argv[1])
        booklist = web_scraping_bot(url)
        print(*booklist, sep='\n')

        # soup = parse_html(get_resource(url))
        # soup.find('div')
        # print(soup.text)
        # print(sys.argv[1], sys.argv[3])
