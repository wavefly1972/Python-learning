# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:24:06 2017

@author: 100419
"""

import pandas as pd
datas=[[65,92,78,83,70],[90,72,76,93,56],[81,85,91,89,77],[79,53,47,94,80]]
indexs=["林大明","陳聰明","黃美麗","熊小娟"]
columns=["國文","數學","英文","自然","社會"]
df=pd.DataFrame(datas,columns=columns,index=indexs)
print(df)
indexs[0]="林晶輝"
df.index=indexs
columns[3]="理化"
df.columns=columns
print(df)
print(df[df.數學>=80])
#print(sorting)
print(df.values)
print(df.values[1][2])
print(df.loc["陳聰明",:])
print(df.loc[("陳聰明","熊小娟"),:])
print(df.loc[("陳聰明","熊小娟"),("數學","理化")])
print(df.loc["陳聰明":"熊小娟","數學":"理化"])
print(df.loc[:"熊小娟","數學":"理化"])
print(df.loc["陳聰明":,"數學":"理化"])