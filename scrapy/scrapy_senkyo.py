#coding:utf-8
from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
from collections import defaultdict

def extract_url(url):
    res = requests.get(url)
    res.encoding = 'Shift-JIS'
    res.text.encode('utf-8')
    soup = bs(res.text, "lxml")
    list_ = soup.find('div', class_='togi17_senkyoku')
    rows = list_.find_all('li')
    url_lists = defaultdict()
    for i in rows:
        a = i.find('a')
        url_lists[a.text] = a.attrs['href']
    return url_lists

def extract_text(url,area):
    global row
    r = requests.get('http://www.tokyo-np.co.jp' + url)
    r.encoding = 'Shift-JIS'
    r.text.encode('utf-8')
    soup = bs(r.text, 'lxml')
    area_status = soup.find('h2',class_='number').text
    area_status = re.split('[:\s|"|]',area_status)
    tables = soup.find('div',{'class':"togi17_table_tod"})
    rows = tables.find_all('li')

    for i in range(len(rows)):
        if ((i+1) %6 == 0) & (i > 5):
            text_tmp = rows[i-5].text.rsplit('（',1)
            df.loc[row,'area'] = area
            df.loc[row,'teisu'] = int(area_status[1])
            df.loc[row,'number'] = int(area_status[3])
            df.loc[row,'name'] = text_tmp[0]
            df.loc[row,'age'] = int(re.sub('[（）]','',text_tmp[1]))
            df.loc[row,'carrer'] = rows[i-4].text
            df.loc[row,'affiliation'] = rows[i-3].text
            df.loc[row,'recommend'] = rows[i-2].text
            df.loc[row, 'status'] = rows[i-1].text
            df.loc[row,'win_count'] = int(rows[i].text)
        row += 1
    return df


if __name__ == '__main__':
    url = 'http://www.tokyo-np.co.jp/senkyo/togisen2017/tod/tod_touha.html'
    url_lists = extract_url(url)
    row = 0
    df = pd.DataFrame(columns = ('area','teisu','number','name','age','carrer','affiliation','recommend','status','win_count',))
    items = url_lists.items()
    for i in items:
        area = i[0]
        url = i[1]
        df = extract_text(url, area)

    df.to_csv('./dataset_senkyo.csv',index=False)
