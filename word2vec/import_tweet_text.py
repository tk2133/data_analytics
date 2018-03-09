#coding:utf-8
import numpy as np
import json
import requests
from requests_oauthlib import OAuth1
import re


access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_key_secret = ''

# タイムライン取得用のURL
url = "https://stream.twitter.com/1.1/statuses/sample.json?language=ja"


def normalize_text(text):
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text = re.sub('RT', "", text)
    text = re.sub('お気に入り', "", text)
    text = re.sub('まとめ', "", text)
    text = re.sub(r'[!-~]', "", text)#半角記号,数字,英字
    text = re.sub(r'[︰-＠]', "", text)#全角記号
    #text = re.sub('\n', "", text)#改行文字
    text = re.sub('\u3000',"", text)
    text = re.sub('\t', "", text)
    text = text.strip()
    return text

# OAuth で GET
auth = OAuth1(consumer_key, consumer_key_secret, access_token, access_token_secret)

with open('~/public_text_twitter.tsv','a', encoding='utf-8') as f:
    res = requests.get(url, auth=auth, stream=True)
    for r in res.iter_lines():
        try:
            r_json = json.loads(r)
            text = r_json['text']
            f.write(normalize_text(text) + '\n')
            n += 1
        except:
            n += 1
            continue
