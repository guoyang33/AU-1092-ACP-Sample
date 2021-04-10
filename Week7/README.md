# 4/9 第七週 | Week 7

## Index

* [4/9 Week 7: 爬蟲2](#49-week-7-crawler-2)
    1. [課堂練習](#課堂練習-Week7)
        * [程式流程](#程式流程-課堂練習-Week7)
        * [程式碼](#程式碼-課堂練習-Week7)
        * [檔案](#檔案-課堂練習-Week7)
        * [輸出檔](#輸出檔-課堂練習-Week7)
    2. [作業](#作業-Week7)
        * [程式流程](#程式流程-作業-Week7)
        * [程式碼](#程式碼-作業-Week7)
        * [檔案](#檔案-作業-Week7)
        * [輸出檔](#輸出檔-作業-Week7)

---

## 4/9 Week 7: Crawler 2

Asia University 1092 Advanced Computer Programming 4/9-Week 7 Crawler

## 課堂練習-Week7

### Introduction-課堂練習-Week7

請同學將課堂練習之 <https://www.majortests.com/word-lists/> 網頁爬蟲程式 Repository 連結及筆記 (Repository 上的 Readme.md 檔) 上傳至系統

### 程式流程-課堂練習-Week7

1. import模組
2. 設定Fetch網址URL
3. 生成Fatch網址List
4. 對網址List迴圈
5. 迴圈中對網址請求
6. 將Response中的body部分使用bs4解析
7. 找出body中的所有class=wordlist的表格table
8. 對7找出的html元素element列表List迴圈
9. 迴圈中再對單一表格找出所有列tr
10. 把列中的各柱(td or th)存入列表
11. 把存有各表格、列與柱的列表寫入engWordList_1.csv

### 程式碼-課堂練習-Week7

~~~~python
import requests
import time
from bs4 import BeautifulSoup
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
~~~~

### 檔案-課堂練習-Week7

[WordListDemo.py](WordListDemo.py)

### 輸出檔-課堂練習-Week7

[engWordList_1.csv](engWordList_1.csv)

---

## 作業-Week7

### Introduction-作業-Week7

請同學以今天課堂練習之範例 針對 <https://csie.asia.edu.tw/project/semester-100> ~ <https://csie.asia.edu.tw/project/108學年> 等網頁抓取資工系畢業專題清單，並將爬找的結果寫入 projectsList.csv 檔中

完成上述任務後，請將 Repository Link 與 筆記說明 上傳至系統

### 程式流程-作業-Week7

1. 因為各學年專題列表的網址並不規則，所以我先從[歷屆專題](https://csie.asia.edu.tw/project)網站，把所需範圍的各網址抓下來存入列表urlx
2. 對urlx迴圈逐一做請求和解析response
3. 把格式化好的資料存入[projectList.csv](projectList.csv)

### 程式碼-作業-Week7

~~~~python
from WordListDemo import get_resource, parse_html
import requests
import csv
import time

def generate_urls(start_page, end_page):
    urls = []
    domain = 'https://csie.asia.edu.tw{0}'
    r = requests.get(domain.format('/project'), verify=False)
    if r.status_code == requests.codes.ok:
        soup = parse_html(r.text)
        for year in range(start_page, end_page+1):
            for item in soup.find(class_='nav-pills').find_all('li'):
                url = item.a.get('href')
                if url.find(str(year)) > -1:
                    urls.append(domain.format(url))
                    break
    else:
        print('catch urls error!!!')
    return urls

def get_projects(soup, count):
    projects = []
    for div in soup.find_all('div', class_='table-responsive'):
        for tr in div.table.find_all('tr'):
            rowData = []
            if count > 1:
                if tr.td != None and tr.td.text.replace('\t', '').replace('\n', '').isnumeric():
                    for cell in tr.find_all('td'):
                        rowData.append(cell.text.replace('\t', '').replace('\n', ''))
                elif tr.th != None and tr.th.text.replace('\t', '').replace('\n', '').isnumeric():
                    for cell in tr.find_all('th'):
                        rowData.append(cell.text.replace('\t', '').replace('\n', ''))
            else:
                if tr.td != None:
                    for cell in tr.find_all('td'):
                        rowData.append(cell.text.replace('\t', '').replace('\n', ''))
                elif tr.th != None:
                    for cell in tr.find_all('th'):
                        rowData.append(cell.text.replace('\t', '').replace('\n', ''))
                count += 1
            projects.append(rowData)
    return projects

def web_scraping_bot(urls):
    projects_list = []
    count = 1
    for url in urls:
        file = url.split('/')[-1]
        print('catching ', file, ' web data...')
        r = get_resource(url)
        if r.status_code == requests.codes.ok:
            soup = parse_html(r.text)
            projects = get_projects(soup, count)
            projects_list = projects_list + projects
            print('waiting 5 seconds...')
            time.sleep(5)
        else:
            print('HTTP requests error!!')
        count += 1
    return projects_list

def save_to_csv(projects, file):
    with open(file, 'w+', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        for project in projects:
            writer.writerow(project)
        

if __name__=='__main__':
    urlx = generate_urls(100, 108)
    projects_list = web_scraping_bot(urlx)
    save_to_csv(projects_list, "projectList.csv")
~~~~

### 檔案-作業-Week7

[GetProjectList.py](GetProjectList.py)

### 輸出檔-作業-Week7

[projectList.csv](projectList.csv)

---
Author: 109021331 CYou Liao
