# 3/26 第五週 | Week 5

## 目錄 | Index
<il>
    <li><a href="https://github.com/guoyang33/AU-1092-ACP-Sample/tree/main/Week5#課堂練習--exercise">課堂練習</a> (Exercise)</li>
    <li><a href="https://github.com/guoyang33/AU-1092-ACP-Sample/tree/main/Week5#作業--homework">作業</a> (Homework)</li>
</il>

# 課堂練習 | Exercise
## 說明 | Introduction
請同學使用 Python抓蟲 去抓 <b>王經篤老師</b> 或 <b>黃明祥老師</b> 的 publication 網頁資料並將資料寫入到資料檔。將操作過程以 Github Repository 的 Readme 進行記錄。將 Github link 上傳至<a href="https://tronclass.asia.edu.tw/">創課平台</a>
<br>
王經篤老師: <a href="http://dns2.asia.edu.tw/~jdwang/PaperList.htm">http://dns2.asia.edu.tw/~jdwang/PaperList.htm</a>
<br>
黃明祥老師: <a href="http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm">http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm</a>
<br>

### Eng. Ver
Make a web-crawler (Worm) to fetch the Publication Page of <b>Teacher Wang</b> or <b>Teacher Huang</b>, and put these data into an output file e.g."output.txt".
<br>
Record all of this step you've done, write it down into "README.md", then submit the Github link to <a href="https://tronclass.asia.edu.tw/">TronClass</a>.
<br>
Teacher Wang: <a href="http://dns2.asia.edu.tw/~jdwang/PaperList.htm">http://dns2.asia.edu.tw/~jdwang/PaperList.htm</a>
<br>
Teacher Huang: <a href="http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm">http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm</a>
<br>

## 程式碼 | Source Code
<pre>
<code>f = open('output-publication.txt', 'w', encoding='utf8')
soup = bs4.BeautifulSoup(rc, 'html.parser')
for tagP in soup.find_all('p', 'MsoNormal'):
    t = tagP.text.replace('\t', '').replace('\n', '')
    f.write(t+'\n')
f.close()
</code></pre>

## 檔案 | Files
<il>
    <li><a href="Exercise.py">Exercise.py</a></li>
    <li><a href="ExerciseEn.py">ExerciseEn.py</a> (Eng. Ver)</li>
</il>

## 輸出檔 | Output File
<il>
    <li><a href="output-publication.txt">output-publication.txt</a></li>
</il>

---
# 作業 | Homework
## 說明 | Introduction
請同學使用 Python 爬蟲程式抓出亞大資工系 103 學年度所有的畢業專題資訊，並將資料寫入到資料檔。
<br>
<a href="https://csie.asia.edu.tw/project/semester-103">https://csie.asia.edu.tw/project/semester-103</a>
<br>
ps. 請開新的 Github repository 完成作業後將 Github link 上傳至<a href="https://tronclass.asia.edu.tw/">創課平台</a>
<br>

### Eng. Ver
Make a web-crawler(Worm) to fetch AU CSIE all of the Infomations of Guaduation Project at 103 School Year, and put these data into an output file, the link is down below.
<br>
<a href="https://csie.asia.edu.tw/project/semester-103">https://csie.asia.edu.tw/project/semester-103</a>
<br>
p.s. Create a new Github repository for this program, submit your Github Repository link to <a href="https://tronclass.asia.edu.tw/">TronClass</a>.
<br>

## 程式碼 | Source Code
<pre>
<code>response.encoding = "utf8"
soup = bs4.BeautifulSoup(response.content, "html.parser")
f = open("output-graduation_projects.txt", "w", encoding="utf8")
for table in soup.find_all("table"):
    for row in table.find_all("tr"):
        for cell in row.find_all("td"):
            t = cell.text.replace("\t", "").replace("\n", "")
            f.write(t+"\t")
        f.write("\n")
    f.write("\n")
f.close()
</code></pre>

## 檔案 | Files
<il>
    <li><a href="Homework.py">Homework.py</a></li>
    <li><a href="HomeworkEn.py">HomeworkEn.py</a> (Eng. Ver)</li>
</il>

## 輸出檔 | Output File
<il>
    <li><a href="output-graduation_projects.txt">output-graduaction_projects.txt</a></li>
</il>

---
Author: 109021331 CYou Liao


<!--
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
-->