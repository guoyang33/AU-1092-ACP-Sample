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
* [3/26 Week 5: 爬蟲1](#326-week-5-crawler-1)
    1. [課堂練習](#課堂練習-Week5)
        * [程式流程](#程式流程-課堂練習-Week5)
        * [程式碼](#程式碼-課堂練習-Week5)
        * [檔案](#檔案-課堂練習-Week5)
        * [輸出檔](#輸出檔-課堂練習-Week5)
    2. [作業](#作業-Week5)
        * [程式流程](#程式流程-作業-Week5)
        * [程式碼](#程式碼-作業-Week5)
        * [檔案](#檔案-作業-Week5)
        * [輸出檔](#輸出檔-作業-Week5)

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

[WordListDemo.py](src/WordListDemo.py)

### 輸出檔-課堂練習-Week7

[engWordList_1.csv](src/engWordList_1.csv)

---

## 作業-Week7

### Introduction-作業-Week7

請同學以今天課堂練習之範例 針對 <https://csie.asia.edu.tw/project/semester-100> ~ <https://csie.asia.edu.tw/project/108學年> 等網頁抓取資工系畢業專題清單，並將爬找的結果寫入 projectsList.csv 檔中

完成上述任務後，請將 Repository Link 與 筆記說明 上傳至系統

### 程式流程-作業-Week7

1. 因為各學年專題列表的網址並不規則，所以我先從[歷屆專題](https://csie.asia.edu.tw/project)網站，把所需範圍的各網址抓下來存入列表urlx
2. 對urlx迴圈逐一做請求和解析response
3. 把格式化好的資料存入[projectList.csv](src/projectList.csv)

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

[GetProjectList.py](src/GetProjectList.py)

### 輸出檔-作業-Week7

[projectList.csv](src/projectList.csv)

---

## 3/26 Week 5: Crawler 1

Asia University 1092 Advanced Computer Programming 3/26-Week 5 Crawler

## 課堂練習-Week5

### Introduction-課堂練習-Week5

請同學使用 Python抓蟲 去抓 王經篤老師 或 黃明祥老師的 publication 網頁資料並將資料寫入到資料檔。將操作過程以 Github Repository 的 Readme 進行記錄。將 Github link 上傳至系統

### 程式流程-課堂練習-Week5

1. 使用瀏覽器進入黃明祥老師的 publication [網頁](http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm)
2. 使用瀏覽器功能「檢視原始碼」以獲得網頁的Html結構
3. 將欲獲取資料之標籤名稱輸入進程式「Python」的bs4篩選條，如「soup.find_all('p', 'MsoNormal')」
4. 程式的寫入流程需配合網頁中欲獲取資料部分的HTML結構進行
5. 程式輸出「output-publication.txt」資料輸出檔

## 程式碼-課堂練習-Week5

~~~~python
import requests as reqs
from bs4 import BeautifulSoup

url = 'http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm' # 黃明祥老師的連結
r = reqs.get(url)
if r.status_code==200:
    r.encoding = 'big5'
    f = open('output-publication.txt', 'w', encoding='utf8')
    soup = BeautifulSoup(r.content, 'html.parser')
    for p in soup.find_all('p', 'MsoNormal'):
        f.write(p.text.replace('\t', '').replace('\n', '')+'\n')
    f.close()
~~~~

### 檔案-課堂練習-Week5

[Exercise.py](src/Exercise.py)

### 輸出檔-課堂練習-Week5

[output-publication.txt](src/output-publication.txt)

---

## 作業-Week5

### Introduction-作業-Week5

請同學使用 Python 爬蟲程式抓出亞大資工系 103 學年度所有的畢業專題資訊，並將資料寫入到資料檔。<https://csie.asia.edu.tw/project/semester-103> ps. 請開新的 Github repository 完成作業後將 Github link 上傳至系統

### 程式流程-作業-Week5

1. 使用瀏覽器進入[亞大資工系 103 學年度所有的畢業專題網站](https://csie.asia.edu.tw/project/semester-103)
2. 使用瀏覽器功能「檢視原始碼」以獲得網頁的HTML結構
3. 將欲獲取資料之標籤名稱輸入進程式「Python」的bs4篩選條，如「soup.find_all('div', 'tab-pane')」
4. 程式的寫入流程需配合網頁中欲獲取資料部分的HTML結構進行
5. 程式輸出「output-projects.txt」資料輸出檔

### 程式碼-作業-Week5

~~~~python
import requests as reqs
from bs4 import BeautifulSoup

url = 'https://csie.asia.edu.tw/project/semester-103'
r = reqs.get(url, verify=False)
if r.status_code==200:
    f = open('output-projects.txt', 'w', encoding='utf8')
    soup = BeautifulSoup(r.content, 'html.parser')
    for div in soup.find_all('div', 'tab-pane'):
        f.write(div.find('h2').text+'\n')
        for tr in div.find_all('tr'):
            for td in tr.find_all('td'):
                f.write(td.text.replace('\t', '').replace('\n', '')+'\t')
            f.write('\n')
        f.write('\n')
    f.close()
~~~~

### 檔案-作業-Week5

[Homework.py](src/Homework.py)

### 輸出檔-作業-Week5

[output-projects.txt](src/output-projects.txt)

---
Author: 109021331 CYou Liao