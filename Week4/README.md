# 3/19 第四週 | Week 4

## 目錄 | Index
<il>
    <li><a href="https://github.com/guoyang33/AU-1092-ACP-Sample/tree/main/Week4#%E8%AA%B2%E5%A0%82%E7%B7%B4%E7%BF%92--exercise">課堂練習</a> (Exercise)</li>
    <li><a href="https://github.com/guoyang33/AU-1092-ACP-Sample/tree/main/Week4#%E4%BD%9C%E6%A5%AD--homework">作業</a> (Homework)</li>
</il>

# 課堂練習 | Exercise
## 說明 | Introduction
請同學將課堂練習的過程記錄在Github的 Repository 中的 Readme 檔案。
<br>
完成後請將 Github Repository 連結上傳至系統
<br>

### Eng. Ver
Record the exercises of class into README.md
<br>
Push your Repository to Github when you finished edit.

## 檔案 | File
<il>
    <li><a href="README.md">README.md</a></li>
</il>

---
# 作業 | Homework
## 說明 | Introduction
請同學使用 Python 爬蟲程式抓出亞大資工系 103 學年度所有的畢業專題資訊，並將資料寫入到資料檔。
<br>
<a href="https://csie.asia.edu.tw/project/semester-103">https://csie.asia.edu.tw/project/semester-103</a>
<br>
ps. 請開新的 Github repository 完成作業後將 Github link 上傳至系統
<br>

### Eng. Ver
Make a web-crawler(Worm) to fetch AU CSIE all of the Infomations of Guaduation Project at 103 School Year, and put these data into an output file, the link is down below.
<br>
<a href="https://csie.asia.edu.tw/project/semester-103">https://csie.asia.edu.tw/project/semester-103</a>
<br>
p.s. Create a new Github repository for this program, submit your Github link to <a href="https://tronclass.asia.edu.tw/">TronClass</a>.
<br>

## 程式碼 | Code Sample
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

## 檔案 | File
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