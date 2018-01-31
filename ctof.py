# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:48:27 2017

@author: 100419
"""

def ctof(c):
    f=c*1.8+32
    return f

inputc=float(input("請輸入攝氏溫度(度C):"))
print("華氏溫度=%5.2f 度F" % ctof(inputc))