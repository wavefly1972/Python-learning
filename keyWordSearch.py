# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:50:09 2017

@author: 100419
"""
import requests
url='https://tw.news.yahoo.com'
html=requests.get(url)
html.encoding="utf-8"
htmllist=html.text.splitlines()
n=0
for row in htmllist:
    if"台灣" in row:n+=1
print("找到{}次" .format(n))
