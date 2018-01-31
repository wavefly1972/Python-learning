# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:40:08 2017

@author: 100419
"""

dict1={"林小明":85,"曾小一":79,"莊孝維":100}
dict1["陳柏霖"]=100
dict1["陳柏澂"]=100
listitem=dict1.item()
for name, score in listitem:
    print("%s的成績為%d分" % (name,score))