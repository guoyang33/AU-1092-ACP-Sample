# 109021331-chenyou-Crawler

## Index

* [4/16 Week 8: 爬蟲3](#416-week-8-crawler-3)
    1. [課堂練習](#課堂練習-----Week-8)
        * [程式流程](#程式流程-課堂練習-----Week-8)
        * [程式碼](#程式碼-課堂練習-----Week-8)
        * [檔案](#檔案-課堂練習-----Week-8)

---

## 4/16 Week 8: Crawler 3

Asia University 1092 Advanced Computer Programming 4/16 Week 8 Crawler

參考：

* [python - Blocked from scraping a website with Scrapy? - Stack Overflow](https://stackoverflow.com/a/59411327)
* [python - How to find tag with particular text with Beautiful Soup? - Stack Overflow](https://stackoverflow.com/questions/9007653/how-to-find-tag-with-particular-text-with-beautiful-soup)

### 課堂練習 --- Week 8

#### Introduction-課堂練習 --- Week8

請同學將課堂上的 博客來網路書店 爬蟲程式完成，並在 Reposity裡的 Readme.md 檔裡將練習過程記錄起來後將 該 Repository 的連結上傳至系統

#### 程式流程-課堂練習 --- Week 8

1. 取得搜尋結果
2. 對每本書分別requests.get()
3. 資料輸出

#### 程式碼-課堂練習 --- Week 8

~~~~python
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from random import randint
import sys
import requests
import time
import csv

URL = 'https://search.books.com.tw/search/query/key/{0}/cat/all'

def generate_search_url(url, keywd):
    return url.format(keywd)

def get_resource(url):
    ua = UserAgent()
    headers = {
        'user-agent': ua.random
    }
    return requests.get(url, headers=headers)

def parse_html(r):
    if r.status_code == requests.codes.ok:
        return BeautifulSoup(r.text, 'lxml')
    else:
        print('HTTP requests error!!')

def get_bd(book_id):
    BDURL = 'https://www.books.com.tw/products/{0}?sloc=main'
    url = BDURL.format(book_id)
    print('Scraping book detail...')
    r = get_resource(url)
    soup = parse_html(r)
    return soup

def web_scraping_bot(url):
    booklist = []
    print('...')
    soup = parse_html(get_resource(url))
    for book in soup.find('table', id='itemlist_table').find_all('tbody'):
        book_id = book.get('id').split('_')[-1]
        book_title = book.find('div', attrs={'class': 'box_1'}).a.get('title')

        # 降低請求頻率以防止伺服器阻擋
        delay = randint(30, 60)
        print('Scraping delay {0} sec...'.format(delay))
        time.sleep(delay)

        bd = get_bd(book_id)
        for item in bd.find('div', attrs={'class': 'type02_p003'}).find_all('li'):
            if '作者' in item.text:
                book_author = item.text.replace('  ', '')[3:]
                break
        book_price = int(bd.find('strong', attrs={'class': 'price01'}).text)
        for item in bd.find('div', attrs={'class': 'bd'}).find_all('li'):
            if 'ISBN' in item.text:
                book_ISBN = item.text.replace('  ', '')[5:]
                break
        
        booklist.append({'book_title': book_title, 'book_author': book_author, 'book_price': book_price, 'book_ISBN': book_ISBN})
    return booklist

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = generate_search_url(URL, sys.argv[1])
        booklist = web_scraping_bot(url)
        print(*booklist, sep='\n')
~~~~

#### 檔案-課堂練習 --- Week 8

* [GetBookList.py](src/GetBookList.py)

---
Author: 109021331 CYou Liao
