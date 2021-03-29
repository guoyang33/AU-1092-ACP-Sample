# -*- coding: utf-8 -*-

"""
Homework.py

作業
程式需要用到的模組: requests、bs4

說明：
此程式執行後會在同目錄下創建或"覆寫"一名為"output-graduation_projects.txt"的檔案
該檔案內容為亞大資工系 103 學年度所有的畢業專題資訊
"""

import requests
import bs4

url = "https://csie.asia.edu.tw/project/semester-103"

# 特別注意的一個點，這裡的requests.get()函式多加一個參數「verify」
# 原因是當程式在向SSL 網站傳送HTTP Request 時，程式會在當前執行環境尋找儲存該網站的安全憑證
# 所以要跳過這個步驟，只要在這用函式時，加入參數「verify」且設為「False」
response = requests.get(url, verify=False)
if response.status_code == 200:
    response.encoding = "utf8"
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    f = open("output-graduation_projects.txt", "w", encoding="utf8")

    # 從原始碼可以得知有兩個表(<table>)的資料要撈，所以使用find_all() 把兩個table 撈出來
    # 再來每個table 有多個行，所以撈tr 也是用find_all()
    # 最後td 的部分，是因為在輸出的時候利用縮進"\t" 來分隔各項資料
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            for cell in row.find_all("td"):
                t = cell.text.replace("\t", "").replace("\n", "")
                f.write(t+"\t")
            f.write("\n")
        f.write("\n")
    f.close()
