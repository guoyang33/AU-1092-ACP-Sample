"""
程式需要用到的模組: requests、bs4、lxml

說明：
此程式執行後會在同目錄下創建或"覆寫"一名為"output-publication.txt"的檔案
該檔案內容為黃明祥老師的網頁上，各著作的標題及著作人
"""

import requests
import bs4

# 設定來源 url
# url = "http://210.70.80.21/~yungchen/1092-Adv-Programming/publication.html" # 周永振老師的連結
# url = "http://dns2.asia.edu.tw/~jdwang/PaperList.htm" # 王經篤老師的連結
url = "http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm" # 黃明祥老師的連結

# 透過requests.get() 函式完成HTTP Request 取得response
response = requests.get(url)

# 設定讀取response 的編碼，除了周永振老師的網頁編碼為utf-8，另外兩位老師的網頁所使用的編碼皆為big5
# response.encoding = 'utf8'
response.encoding = 'big5'

# 從response 中取得HTML 原始碼，即為response 的content 屬性
# 其類型(type)為字串(str)
rc = response.content # 存入變數rc

# 使用bs4 函式庫中的BeautifulSoup 函式將字串型態(str)的HTML 文本轉成程式好解讀的物件型態(object)
# 此函式第2的參數是解析文本的方式，其細節可上網搜尋
soup = bs4.BeautifulSoup(rc, 'html.parser') # 使用html.parser 解析
# soup = bs4.BeautifulSoup(rc, 'lxml') # 使用lxml 解析 (需另外安裝lxml 模組)

# 檢查response 的網頁HTTP 狀態碼，可透過response 中的status_code 屬性取得
# 常見的狀碼與對應的意思有：200:OK, 404:Page Not Found, 500:Server Internal Error
if response.status_code == 200: # 狀態碼 200代表正常

    # 將要改寫的輸出記錄檔打開，若不存在則會自動建立
    # 參數1: 檔名, 參數2: 開啓模式(r:讀, w:寫)
    # 參數encoding 即為檔案編碼，使用utf-8 萬國碼可在大多編碼的檢視中正常顯示
    f = open('output-publication.txt', 'w', encoding='utf8')

    # 此程式是以爬蟲黃明祥老師的網頁為例，不同的網頁會有不同的HTML 結構
    # 所以在使用soup.find 或是soup.find_all 時要視情況而定
    # soup 中的find()與find_all() 方法(Method)的第一個參數都是選擇的標籤名稱，第二個則是該元素的class 名稱
    # find()回傳值是符合條件的第一個HTML物件；find_all() 的回傳則是符合條件的所有HTML 物件，為列表型態(list)
    
    # 在黃明祥老師的網頁原始碼中，可以看到針對Publication 的每筆資料都是用<p class="MsoNormal">這個標籤包起來的
    # 所以使用soup 物件(object)中的find_all()方法(Method)，要符合的條件為：標籤名稱為<p>且class="MsoNormal"
    # 而因為是列表型態(list) 所以可以使用for 迴圈迭代出每一筆資料
    for tagP in soup.find_all('p', 'MsoNormal'):

        # 註：使用bs4 解析HTML 後回傳的 HTML物件，不管有沒有經過find() 或find_all() 的篩選
        # 此型態(type) 皆有一屬性(Attribute)就叫text，其值為該HTML 物件的字串(str) 型態(type)
        # 還會自動去掉所有的標籤(也就是<xxx></xxx>)

        # 得到每一筆的Publication 資料後，就把多餘的字符去掉，如：「換行字符"\n"和縮進字符"\t"等」
        # 這裡的作法是先用HTML 物件中的text 屬性去掉標籤名稱，再用字串(str)的內建方法replace()把"\n"及"\t"去掉
        t = tagP.text.replace('\t', '').replace('\n', '')

        # 把上面處理完的"干淨"的資料寫入前面打開的檔案中，記得在行尾加上"\n"
        # 這裡的"\n" 跟上面被去掉的"\n"是兩回事，上面去掉的是原本應該要在一行的文字因為被bs4 解析後所加上的"\n"
        # 不去掉會導致現在在這裡的資料呈現應該同一行的文字跳到下一行
        f.write(t+'\n')

    # 最後的最後，把開啓的檔案關閉
    f.close()
