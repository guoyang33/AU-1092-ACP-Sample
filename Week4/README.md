# 3/19 第四週 | Week 4

## 目錄 | Index
<il>
    <li><a href="https://github.com/guoyang33/AU-1092-ACP-Sample/tree/main/Week4#課堂練習--exercise">課堂練習</a> (Exercise)</li>
    <li><a href="https://github.com/guoyang33/AU-1092-ACP-Sample/tree/main/Week4#homework">Homework</a></li>
</il>

# 課堂練習 | Exercise
## 說明 | Introduction
請同學將課堂練習的過程記錄在Github的 Repository 中的 Readme 檔案。
<br>
完成後請將 Github Repository 連結上傳至<a href="https://tronclass.asia.edu.tw/">創課平台</a>
<br>

### Eng. Ver
Record the exercises of class into "README.md".
<br>
Submit Github Repository link to <a href="https://tronclass.asia.edu.tw/">TronClass</a>.

## 檔案 | Files
<il>
    <li><a href="README.md">README.md</a></li>
</il>

---
# Homework
## 說明 | Introduction
請同學將作業以一個 Github 的 Repository 整理後並在 Readme 檔案裡加入筆記說明，再將 Repository 的 連結上傳至<a href="https://tronclass.asia.edu.tw/">創課平台</a>

### Eng. Ver
Arrange a Github Repository, and write down the introduction into "README.md", then submit this Github Respository link to <a href="https://tronclass.asia.edu.tw/">TronClass</a>.

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