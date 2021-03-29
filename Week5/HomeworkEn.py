# -*- coding: utf-8 -*-

"""
HomeworkEn.py

Homework
Required modules: requests, bs4

Introduction:
After run this program, it will create or overwite named "output-graduation_projects.txt" file on the same directory of this program.
In that file, this program will write the Infomations from Asia University CSIE Graduation Projects in 103 School Year
"""

import requests
import bs4

url = "https://csie.asia.edu.tw/project/semester-103"

# Here's the point, I set parameter "verify" of requests.get() function to "False" it's because
# When you do HTTP Request to a SSL site, your browser will try to find Secure Certification on your python vironment, but there's a unsafe way to skip this step is to disable this verify action
# So I set this "verify" parameter to False
response = requests.get(url, verify=False)
if response.status_code == 200:
    response.encoding = "utf8"
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    f = open("output-graduation_projects.txt", "w", encoding="utf8")

    # When you view the source HTML of the website, as you can see, there's two tables of data, then you can use find_all() to get those table
    # In the table, there's multiple row in it, so you can keep using find_all() to get those rows
    # Final step, because I want to add indent "\t" behind each data, then, I use find_all() to get each cell, then add indent while write data in output file
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            for cell in row.find_all("td"):
                t = cell.text.replace("\t", "").replace("\n", "")
                f.write(t+"\t")
            f.write("\n")
        f.write("\n")
    f.close()
