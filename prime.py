# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:21:43 2017

@author: 100419
"""

n=int(input("請輸入大於1的整數："))
if(n==2):
    print("%d是質數!" % n)
else:
    for i in range(2,n):
        if(n%i==0):
            print("%d不是質數!" % n)
            break
    else:print("%d是質數!!" % n)