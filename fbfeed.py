# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:44:57 2017

@author: 100419
"""

import requests,json

url="https://graph.facebook.com/v2.7/838133046237454/posts?fields=created_time%2Cmessage&limit=25&since=1509776909&__paging_token=enc_AdAc1ZA8JTP2Enx9zAr2NOG7rWNaLOfb1wJOHjfdCxForW5ck5tQxiZBYuzFx5ZAGy2RxH8ReNbBm2rEMWsUcXSvVf33S8TlozXPKf1m7kVSNyi2QZDZD&__previous=1&access_token=EAACEdEose0cBAE1KXs67ZCiouwSlopKXq0lpVdw7htnJfwrHHFfGWSS37KkjkeZCKhyle1RlkzRBIngchNZAUbNwPKOz7aMNauGI5TcuxJu8ZC2CqhD4sfHmMl0IhHhzxZA3omPDxIulIBlhI0mdTplXewjlXDzpWL17P5yAjajoiLQR5EZA27AbgFl9aiQPQZD"

data=json.loads(requests.get(url).text)

for d in data['data']: #讀取Key名稱為data的字典
    if 'message' in d: #確認message存在
        print("message:{}" .format(d['message']))
        print("created time:{}" .format(d['created_time']))
        print("id:{}".format(d['id']))
        print()