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
print(df.iloc[1,:])
print(df.iloc[1][2])
#print(df.ix[:"熊小娟","數學":"理化"])
print(df.head(2))
print(df.tail(2))
#df.loc["陳聰明",:]=80
#print(df.loc["陳聰明",:])
#df.loc[("陳聰明","熊小娟"),("數學","理化")]=80
#print(df.loc[("陳聰明","熊小娟"),("數學","理化")])
#print(df)
df1=df.sort_values(by="數學",ascending=False)
print(df1)
df2=df.drop("陳聰明")
print(df2)
df3=df.drop(["數學","理化"],axis=1)
print(df3)
df4=df.drop(df.index[1:4],axis=0)
print(df4)
df5=df.drop(df.columns[1:4],axis=1)
print(df5)















