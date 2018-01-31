# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:10:28 2017

@author: 100419
"""

import sqlite3,ast,hashlib,os,requests
from bs4 import BeautifulSoup

conn=sqlite3.connect('DataBasePM25.sqlite') #建立資料庫連線
cursor=conn.cursor() #建立cursor物件

#建立一個資料表
sqlstr='''
CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,"SiteName" TET NOT NULL, "PM25" INTEGER)
'''
cursor.execute(sqlstr)

url="http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&skip=0&$top=1000&format=json"
#讀取網頁原始碼
html=requests.get(url).text.encode('utf-8-sig')

#判斷網頁是否更新
md5=hashlib.md5(html).hexdigest()
old_md5=""

if os.path.exists('old_md5.txt'):
    with open('old_md5.txt','r') as f:
        old_md5=f.read()
    with open('old_md5.txt','w') as f:
        f.write(md5)

if md5 != old_md5:
    print('資料已更新')
    sp=BeautifulSoup(html,'html.parser')
    #將網頁內轉換為 list,list中的元素是dict
    jsondata=ast.literal_eval(sp.text)
    #刪除資料表內容
    conn.execute("delete from TablePM25")
    conn.conmmit()
    
    n=1
    for site in jsondata:
        SiteName=site["SiteName"]
        PM25=0 if site["PM2.5"] == "" else int(site["PM2.5"])
        print("站名:{} PM2.5={}" .format(SiteName,PM25))
        #新增一筆紀錄
        sqlstr="insert into TablePM25 values({},'{}',{})".format(n,SiteName,PM25)
        cursor.execute(sqlstr)
        n+=1
        conn.commit()
        
else:
    print('資料未更新，從資料庫讀取')
    cursor=conn.execute("select * from TablePM25")
    rows=cursor.fetchall()
    for row in rows:
        print("站名:{} PM2.5={}" .format(row[1],row[2]))
    
conn.close()
        