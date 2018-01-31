# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:59:26 2017

@author: 100419
"""

pw=input("請輸入密碼:")
if(pw=="1234"):
    print("歡迎光臨!!")
else:
    print("密碼錯誤!!")

score=input("請輸入成績:")
if(int(score)>=90):
    print("優等")
elif(int(score)>=80):
    print("甲等")
elif(int(score)>=70):
    print("乙等")
elif(int(score)>=60):
    print("丙等")
else:print("丁等")