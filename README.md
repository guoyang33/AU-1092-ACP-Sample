# 1092 Asia University Advanced Computer Programming Sample
Code sample for Asia University 1092 Advanced Computer Programming.
<br/>
Author: 109021331 CYou Liao
## 注意 | Notice
各程式需要用到的模組我會寫在程式碼開頭，檢查模組是否已安裝的方法如下
<br/>
執行程式後看有報此錯誤碼
<pre><code>Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'</code></pre>
則代表模組requests尚未安裝
<br/>
也可以在終端機中輸入
<pre><code>pip show <模組名稱></code></pre>
回傳 <code>WARNING: Package(s) not found: <模組名稱></code>
就是模組未安裝
<br/>若要安裝模組，在終端機中輸入
<pre><code>pip install <模組名稱></code></pre>
若以上指令沒用，嘗試：
<pre><code>python -m pip install <模組名稱></code></pre>
還是沒用的話，就要把 Python 重新安裝，且在安裝過程中勾選「Add Python to PATH」
<img src="imgs/0001_add_Python_>

# 3/26 第五週 | Week 5
<a href="week5">資料夾</a> (Folder)
## 課堂練習 | Exercise
### 說明 | Introduction
請同學使用 Python抓蟲 去抓 <b>王經篤老師</b> 或 <b>黃明祥老師</b> 的 publication 網頁資料並將資料寫入到資料檔。將操作過程以 Github Repository 的 Readme 進行記錄。將 Github link 上傳至系統
<br/>
王經篤老師: <a href="http://dns2.asia.edu.tw/~jdwang/PaperList.htm">http://dns2.asia.edu.tw/~jdwang/PaperList.htm</a>
<br/>
黃明祥老師: <a href="http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm">http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm</a>
<br/>
#### Eng. Ver
Make a web-crawler (worm) to fetch the Publication Page of <b>Teacher Wang</b> or <b>Teacher Huang</b>, and put these data into an output file e.g."output.txt".
<br/>
Record all of this step you've done, write in to your "README.md".
<br/>
Submit the Github link to <a href="https://tronclass.asia.edu.tw/">TronClass</a>
<br/>
Teacher Wang: <a href="http://dns2.asia.edu.tw/~jdwang/PaperList.htm">http://dns2.asia.edu.tw/~jdwang/PaperList.htm</a>
<br/>
Teacher Huang: <a href="http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm">http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm</a>
<br/>

### 程式碼 | Code Sample
<a href="week5/Exercise.py">Link</a>
## 作業 | Homework

