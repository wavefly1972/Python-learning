# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:30:48 2017

@author: 100419
"""

from bs4 import BeautifulSoup
import requests
url='http://www.e-happy.com.tw'
html=requests.get(url)
html.encoding="utf-8"
sp=BeautifulSoup(html.text,"html.parser")
links=sp.find_all(["a","img"])
for link in links:
    href=link.get("href")
    if href != None and href.startswith("http://"):
        print(href)