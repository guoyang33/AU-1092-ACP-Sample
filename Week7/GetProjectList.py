# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import csv
import time

def generate_urls(start_page, end_page):
    urls = []
    domain = 'https://csie.asia.edu.tw{0}'
    r = requests.get(domain.format('/project'), verify=False)
    if r.status_code == requests.codes.ok:
        soup = parse_html(r.text)
        for year in range(start_page, end_page+1):
            for item in soup.find(class_='nav-pills').find_all('li'):
                url = item.a.get('href')
                if url.find(str(year)) > -1:
                    urls.append(domain.format(url))
                    break
    else:
        print('catch urls error!!!')
    return urls

def get_resource(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64: x64) ApplWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    return requests.get(url, headers=headers, verify=False)

def parse_html(html_str):
    return BeautifulSoup(html_str, 'lxml')

def get_projects(soup, count):
    projects = []
    for div in soup.find_all('div', class_='table-responsive'):
        for tr in div.table.find_all('tr'):
            rowData = []
            if count > 1:
                if tr.td != None and tr.td.text.replace('\t', '').replace('\n', '').isnumeric():
                    for cell in tr.find_all('td'):
                        rowData.append(cell.text.replace('\t', '').replace('\n', ''))
                elif tr.th != None and tr.th.text.replace('\t', '').replace('\n', '').isnumeric():
                    for cell in tr.find_all('th'):
                        rowData.append(cell.text.replace('\t', '').replace('\n', ''))
            else:
                if tr.td != None:
                    for cell in tr.find_all('td'):
                        rowData.append(cell.text.replace('\t', '').replace('\n', ''))
                elif tr.th != None:
                    for cell in tr.find_all('th'):
                        rowData.append(cell.text.replace('\t', '').replace('\n', ''))
                count += 1
            projects.append(rowData)
    return projects

def web_scraping_bot(urls):
    projects_list = []
    count = 1
    for url in urls:
        file = url.split('/')[-1]
        print('catching ', file, ' web data...')
        r = get_resource(url)
        if r.status_code == requests.codes.ok:
            soup = parse_html(r.text)
            projects = get_projects(soup, count)
            projects_list = projects_list + projects
            print('waiting 5 seconds...')
            time.sleep(5)
        else:
            print('HTTP requests error!!')
        count += 1
    return projects_list

def save_to_csv(projects, file):
    with open(file, 'w+', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        for project in projects:
            writer.writerow(project)
        

if __name__=='__main__':
    urlx = generate_urls(100, 108)
    projects_list = web_scraping_bot(urlx)
    save_to_csv(projects_list, "projectList.csv")