# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:43:19 2017

@author: 100419
"""

#import matplotlib.pyplot as plt
from bokeh.plotting import figure,show
from bs4 import BeautifulSoup as bs
import requests

year=[]
#year2=[]
person=[]
#person2=[]
url="http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content=requests.get(url).text
parse=bs(content,"html.parser")
data1=parse.select("table[summary^='歷年戶數統計列表排版用']")[0]
print(data1)
rows=data1.find_all("tr")
for row in rows:
    cols=row.find_all("td")
    if(len(cols)>0):
        if cols[1].text != "--":
            year.append(int(cols[0].text[:-1]))
            person.append(cols[1].text)
        
p=figure(width=800,height=400,title="Taoyan Daxi population")   
#p.title_text_font_size="20pt"
p.xaxis.axis_label="year"
p.yaxis.axis_label="house"
p.line(year,person,line_width=2) 
show(p)     
#year.reverse()
#person.reverse()
#plt.plot(year,person,lw=2.0)
#plt.title("Taoyuan Population")
#plt.xlabel("year")
#plt.ylabel("house")
#plt.legend()
#plt.show()