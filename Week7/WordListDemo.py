# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import csv

URL = 'https://www.majortests.com/word-lists/word-list-0{0}.html'

def generate_urls(url, startPage, endPage):
    urls = []
    for i in range(startPage, endPage):
        urls.append(url.format(i))
    return urls

def get_resource(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64: x64) ApplWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    return requests.get(url, headers=headers, verify=False)

def parse_html(html_str):
    return BeautifulSoup(html_str, 'lxml')

def get_words(soup, file):
    words = []
    count = 0
    for wordlist_table in soup.find_all(class_='wordlist'):
        count += 1
        for word_entry in wordlist_table.find_all('tr'):
            new_word = []
            new_word.append(file)
            new_word.append(str(count))
            new_word.append(word_entry.th.text)
            new_word.append(word_entry.td.text)
            words.append(new_word)
    return words

def web_scraping_bot(urls):
    eng_words = []
    for url in urlx:
        file = url.split('/')[-1]
        print('catching: ', file, ' web data...')
        r = get_resource(url)
        if r.status_code == requests.codes.ok:
            soup = parse_html(r.text)
            words = get_words(soup, file)
            eng_words = eng_words + words
            print('waiting 5 seconds...')
            time.sleep(5)
        else:
            print('HTTP requests error!!')
    return eng_words

def save_to_csv(words, file):
    with open(file, 'w+', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)


if __name__ == '__main__':
    urlx = generate_urls(URL, 1, 3)
    eng_words = web_scraping_bot(urlx)
    save_to_csv(eng_words, "engWordList_1.csv")