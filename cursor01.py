# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:45:30 2017

@author: 100419
"""

import sqlite3
conn=sqlite3.connect('test.sqlite') #建立資料庫連線
cursor=conn.cursor() #建立cursor物件
#建立一個資料表
sqlstr='CREATE TABLE IF NOT EXISTS table01("num" INTEGER PRIMARY KEY NOT NULL, "tel" TEXT)'
cursor.execute(sqlstr)

#新增一筆記錄
#sqlstr='insert into table01 values(1,"02-1234567")'
#cursor.execute(sqlstr)
#conn.commit() #主動更新

#新增一筆資料，資料內容為"num=1,tel='02-1234567'
num=1
tel="02-1234567"
sqlstr="insert into table01 values({},'{}')".format(num,tel)
conn.execute(sqlstr)
conn.commit()

#更新table01資料表，num=1 的這筆資料為 tel="049-5711438"
sqlstr="update table01 set tel='{}' where num={}".format("049-29880000",1)
conn.execute(sqlstr)
conn.commit()
conn.close()
#