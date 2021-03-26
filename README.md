# 1092 Asia University Advanced Computer Programming Sample
Code sample for Asia University 1092 Advanced Computer Programming.
<a href="#注意-python--notice-for-python">頁底</a>

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

## 注意 (Python) | Notice (For Python)
各程式需要用到的模組我會寫在程式碼開頭，檢查模組是否已安裝的方法如下
<br/>
The required modules in program, I wrote it on the top of the source code, to check the module are installed, follow the stpes below:
<br/>
<br/>
執行程式後看有報此錯誤碼
<br/>
Run .py file and if you see Terminal return this error message
<pre><code>Traceback (most recent call last):
  File "&#60;stdin&#62;", line 1, in <module>
ModuleNotFoundError: No module named 'requests'</code></pre>
則代表模組 requests 尚未安裝
<br/>
In this case, that means module "requests" doesn't installed
<br/>
<br/>
也可以在終端機中輸入
<br/>
You also can type the command below into Terminal
<pre><code>pip show <模組名稱 (Module Name)></code></pre>
以下回傳訊息也是模組未安裝的意思
<br/>
If Terminal return the message below, it also means module doesn't installed
<pre><code>WARNING: Package(s) not found: <模組名稱 (Module Name)></code></pre>

<br/>
若要安裝模組，在終端機中輸入
<br/>
To install the module, type the command below into Terminal
<pre><code>pip install <模組名稱 (Module Name)></code></pre>
若以上指令沒用，嘗試：
If the command above not working, try this
<pre><code>python -m pip install <模組名稱 Module Name></code></pre>
還是沒用的話，就要把 Python 重新安裝，且在安裝過程中勾選「Add Python to PATH」詳細可參考<a href="https://medium.com/codingbar/%E8%87%AA%E5%AD%B8python%E7%9A%84%E7%AC%AC%E9%9B%B6%E8%AA%B2-%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%9Dpython%E7%92%B0%E5%A2%83-7eeeb1642889">此連結</a>
<br/>
If still not working, then you should reinstall Python, and while you installing, be sure you checked the box called something like "Add python to PATH". To know more detail you can found it in this <a href="https://datatofish.com/add-python-to-windows-path/">link</a>
<img src="imgs/0001_add_Python_to_Path.png">
<br/>
安裝完後再將電腦重新啓動
<br/>
Then reboot your computer when you finished install

---
Author: 109021331 CYou Liao