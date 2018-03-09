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
    list_ = soup.find('div', class_='togi17_senkyoku')
    rows = list_.find_all('li')
    url_lists = defaultdict()
    for i in rows:
        a = i.find('a')
        url_lists[a.text] = a.attrs['href']
    return url_lists


def extract_text(url, area, df):
    global row
    r = requests.get('http://www.tokyo-np.co.jp' + url)
    soup = bs(r.content, 'html.parser')
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
            df.loc[row,'name'] = text_tmp[0].replace(' ','').replace('　','')
            df.loc[row,'age'] = int(re.sub('[（）]','',text_tmp[1]))
            df.loc[row,'carrer'] = rows[i-4].text
            df.loc[row,'affiliation'] = rows[i-3].text
            df.loc[row,'recommend'] = rows[i-2].text
            df.loc[row, 'status'] = rows[i-1].text
            df.loc[row,'win_count'] = int(rows[i].text)
        row += 1
    return df

url = 'http://k-db.com/stocks/'
res = requests.get(url)
soup = bs(res.content, "html.parser")
soup
if __name__ == '__main__':
    url = 'http://www.tokyo-np.co.jp/senkyo/togisen2017/tod/tod_touha.html'
    url_lists = extract_url(url)
    row = 0
    df = pd.DataFrame()
    items = url_lists.items()
    for i in items:
        area = i[0]
        url = i[1]
        df = extract_text(url, area, df)

    df.to_csv('./dataset_senkyo.csv',index=False)
