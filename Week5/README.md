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
Record all of this step you've done, write in to your "README.md".
<br>
Submit the Github link to <a href="https://tronclass.asia.edu.tw/">TronClass</a>.
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