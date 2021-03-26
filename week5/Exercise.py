"""
程式需要用到的模組: requests、bs4、lxml

This program required modules: requests, bs4, lxml
"""

import requests
import bs4

# 設定來源 url
# url = "http://210.70.80.21/~yungchen/1092-Adv-Programming/publication.html" # 周永振老師的連結
# url = "http://dns2.asia.edu.tw/~jdwang/PaperList.htm" # 王經篤老師的連結
url = "http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm" # 黃明祥老師的連結

# 透過requests.get 函式完成http request 取得response
response = requests.get(url)

# 設定讀取response 的編碼，除了周永振老師的網頁編碼為utf-8，另外兩位老師的網頁所使用的編碼皆為big5
# response.encoding = 'utf8'
response.encoding = 'big5'

# 從response 中取得html 原始碼，即為response 的content 屬性
# 其類型(type)為字串(str)
rc = response.content # 存入變數rc

# 使用bs4 函式庫中的BeautifulSoup 函式將字串型態(str)的html 文本轉成程式好解讀的物件型態(object)
# 此函式第2的參數是解析文本的方式，其細節可上網搜尋
# soup = bs4.BeautifulSoup(rc, 'lxml') # 使用lxml 解析
soup = bs4.BeautifulSoup(rc, 'html.parser') # 使用html.parser 解析

# 檢查response 的網頁HTTP 狀態碼，可透過response 中的status_code 屬性取得
# 常見的狀碼與對應的意思有：200:OK, 404:Page Not Found, 500:Server Internal Error
if response.status_code == 200: # 狀態碼 200代表正常
    # 將要改寫的輸出記錄檔打開，若不存在則會自動建立
    # 參數1: 檔名, 參數2: 開啓模式(r:讀, w:寫)
    # 參數encoding 即為檔案編碼，使用utf-8 萬國碼可在大多編碼的檢視中正常顯示
    f = open('output-publication.txt', 'w', encoding='utf8')

    for li in soup.find_all('p', 'MsoNormal'):
        t = li.text.replace('\t', '').replace('\n', '')
        # t = li.text.replace('  ', '').replace('	', '').replace('\t', '').replace('\n', '')
        # t = li.text.replace('\n', '')
        # t = t.replace(' ', '')
        print(t)
        f.write(t+'\n')
    f.close()

# print(soup.find('div', id='home').find_all('li'))


# print(soup.body)
# print(soup.find('div', id='home'))

# print(soup.find("ol", "pubList").find_all("li"))


# print(response.status_code)
# print(response.content)

# print(bs4.BeautifulSoup(response.content, 'html.parser'))
