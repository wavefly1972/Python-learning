# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:10:28 2017

@author: 100419
"""

import sqlite3,ast,hashlib,os,requests
from bs4 import BeautifulSoup

cur_path=os.path.dirname(__file__)  #取得目前路徑
conn=sqlite3.connect(cur_path + '/' + 'DataBaseAQI2.sqlite') #建立資料庫連線
cursor=conn.cursor() #建立cursor物件

#建立一個資料表
sqlstr='''
CREATE TABLE IF NOT EXISTS TableAQI ("no" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,"SiteName" TET NOT NULL, "AQI" INTEGER)
'''
cursor.execute(sqlstr)

#url="http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&skip=0&$top=1000&format=json"
url="http://opendata.epa.gov.tw/ws/Data/ATM00679/?$orderby=MonitorDate%20desc&$skip=0&$top=1000&format=json"
#讀取網頁原始碼
html=requests.get(url).text.encode('utf-8-sig')

#判斷網頁是否更新
#md5=hashlib.md5(html).hexdigest()
#old_md5=""

#if os.path.exists('old_md5.txt'):
    #with open('old_md5.txt','r') as f:
        #old_md5=f.read()
    #with open('old_md5.txt','w') as f:
        #f.write(md5)

#if md5 != old_md5:
print('資料已更新')
sp=BeautifulSoup(html,'html.parser')
    #將網頁內轉換為 list,list中的元素是dict
jsondata=ast.literal_eval(sp.text)
    #刪除資料表內容
conn.execute("delete from TableAQI")
conn.commit()
    
n=1
for site in jsondata:
    SiteName=site["SiteName"]
    AQI=0 if site["AQI"] == "" else int(site["AQI"])
    print("站名:{} AQI={}" .format(SiteName,AQI))
        #新增一筆紀錄
    sqlstr="insert into TableAQI values({},'{}',{})".format(n,SiteName,AQI)
    cursor.execute(sqlstr)
    n+=1
    conn.commit() #主動更新
        
#else:
    #print('資料未更新，從資料庫讀取')
    #cursor=conn.execute("select * from TableAQI")
    #rows=cursor.fetchall()
    #for row in rows:
        #print("站名:{} AQI={}" .format(row[1],row[2]))
    
conn.close()
        