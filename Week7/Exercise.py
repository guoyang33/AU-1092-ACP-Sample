# -*- coding: utf-8 -*-

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