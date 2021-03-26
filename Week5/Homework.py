import requests
import bs4

url = "https://csie.asia.edu.tw/project/semester-103"
response = requests.get(url, verify=False)
if response.status_code == 200:
    response.encoding = "utf8"
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    f = open("output-graduation_project.txt", "w", encoding="utf8")

    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            for cell in row.find_all("td"):
                t = cell.text.replace("\t", "").replace("\n", "")
                f.write(t+"\t")
            f.write("\n")
        f.write("\n")
    f.close()
