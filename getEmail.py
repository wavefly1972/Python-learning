# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:21:42 2017

@author: 100419
"""

import requests,re
regex=re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
url='https://auth.cht.com.tw/ldaps/'
html=requests.get(url)
emails=regex.findall(html.text)
for email in emails:
    print(email)