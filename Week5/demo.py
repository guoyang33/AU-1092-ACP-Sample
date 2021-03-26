import requests
import bs4

response = requests.get("http://210.70.80.21/~yungchen/1092-Adv-Programming/publication.html")
response.encoding = 'utf8'
# response.encoding = 'big5'
rc = response.content
# soup = bs4.BeautifulSoup(rc, 'html.parser')
soup = bs4.BeautifulSoup(rc, 'lxml')

if response.status_code == 200:
    f = open('output14.txt', 'w', encoding='utf8')
    # f.write(soup.find('div', id='home').text)
    # for li in soup.find('div', id='home').find_all('li'):
    for li in soup.find_all('li'):
        # t = li.text.replace('  ', '').replace('	', '').replace('\t', '').replace('\n', '')
        t = li.text.replace('\n', '')
        t = t.replace(' ', '')
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
