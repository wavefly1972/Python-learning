# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:22:03 2017

@author: 100419
"""

import hashlib,requests,os
#from bs4 import BeautifulSoup
#from urllib.request import urlopen

url='http://www.tooopen.com/img/87.aspx'
#讀取網頁原始碼
html=requests.get(url).text.encode('utf-8-sig')
#判斷網頁是否更新
md5=hashlib.md5(html).hexdigest()
if os.path.exists('old_md5.txt'):
    with open('old_md5.txt','r') as f:
        old_md5=f.read()
    with open('old_md5.txt','w') as f:
        f.write(md5)

else:
    with  open('old_md5.txt','w') as f:
        f.write(md5)
    
if md5 != old_md5:
    print('資料已更新!')
else:
    print('資料未更新,從資料庫讀取')
