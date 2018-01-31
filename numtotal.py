# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:38:49 2017

@author: 100419
"""
sum=0
n=int(input("請輸入正整數:"))
for i in range(1,n+1):
    sum+=i
print("1 到 %d 的整數和為 %d " % (n,sum))