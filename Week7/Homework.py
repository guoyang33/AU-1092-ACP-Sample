# -*- coding: utf-8 -*-

"""
使用到的library
requests
bs4

執行程式後會在同目錄下產生一檔案案「output-projects.txt」
其內容為「亞大資工系 103 學年度所有的畢業專題資訊」
"""

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