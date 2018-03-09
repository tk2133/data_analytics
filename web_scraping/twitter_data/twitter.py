#coding:utf-8
import numpy as np
import json
import requests
from requests_oauthlib import OAuth1Session
from datetime import datetime

access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_key_secret = ''

# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# とくにパラメータは無い
max_id = 1
params = {'screen_name':'ozwspw',
          'exclude_replies':True,
          'include_entities':False,
          'include_rts':False,
          'count':200}

# OAuth で GET
twitter = OAuth1Session(consumer_key, consumer_key_secret, access_token, access_token_secret)
f_out = open('/text_ozawa_twitter.tsv','w')

for j in range(100):
    res = twitter.get(url, params = params)

    if res.status_code == 200:

        # API残り
        limit = res.headers['x-rate-limit-remaining']
        if limit == 1:
            break
            #sleep(60*16)
        # API制限の更新時刻 (UNIX time)
        #reset = res.headers['x-rate-limit-reset']

        print ("API remain: " + limit)
        #print ("API reset: " + reset)

        n = 0
        timeline = json.loads(res.text)
        print(len(timeline))
        # 各ツイートの本文を表示
        for i in range(len(timeline)):
            if i != len(timeline)-1:
                f_out.write(timeline[i]['text'] + '\n')
            else:
                f_out.write(timeline[i]['text'] + '\n')
                params['max_id'] = timeline[i]['id']-1

f_out.close()
