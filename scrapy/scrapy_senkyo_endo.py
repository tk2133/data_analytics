#coding:utf-8
from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
from collections import defaultdict
#pip install chardet

def extract_url(url):
    res = requests.get(url)
    soup = bs(res.content, "html.parser")
    list_ = soup.find('div',id= 'SubLink2')
    rows = list_.find_all('li')
    url_lists = defaultdict()
    for i in rows:
        a = i.find('a')
        url_lists[a.text] = a.attrs['href']
    return url_lists

def make_win_list(url):
    global win_lists
    res = requests.get('http://www.asahi.com/' + url)
    soup = bs(res.content, "html.parser")
    table = soup.find('table', class_='SnkTbl01')
    a = table.find_all('tr')
    for i in a:
        if i.find('img', alt = '当選') is not None:
            name = i.find('td', class_="Name")
            win_lists.append(name.text)


if __name__ == '__main__':
    url = 'http://www.asahi.com/senkyo/togisen/2017/kaihyo/'
    url_lists = extract_url(url)
    items = url_lists.items()
    win_lists = []
    for i in items:
        area = i[0]
        url = i[1]
        make_win_list(url)

    with open('./win_list.tsv', 'w') as f:
        for name in win_lists:
            f.write(name.replace('　','') + '\n')
