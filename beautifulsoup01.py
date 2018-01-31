# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:01:09 2017

@author: 100419
"""

import requests
from bs4 import BeautifulSoup
url='http://www.taiwanlottery.com.tw/'
html=requests.get(url)
sp=BeautifulSoup(html.text,'html.parser')
data1=sp.select("title")
data2=sp.select("#rightdown")
#<p class="title><b>文件標題</b></p>
data3=sp.select(".title")
data4=sp.select("html head title")
#print(data1)
#print(data2)
print(data3)
#print(data4)