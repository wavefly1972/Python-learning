# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:23:43 2017

@author: 100419
"""

from bokeh.plotting import figure,show
p=figure(width=800,height=400,title="Money per day")
p.title.text_color="green"
p.title.text_font_size="20pt"
p.xaxis.axis_label="age"
p.xaxis.axis_label_text_color="violet"
p.yaxis.axis_label="money"
p.yaxis.axis_label_text_color="violet"

dashs=[12,4]
listx1=[1,5,7,13,16]
listy1=[15,30,50,60,80,90]
p.line(listx1,listy1,line_width=4,line_color="red",line_alpha=0.3,line_dash=dashs,legend="Male")

listx2=[1,5,7,13,16]
listy2=[15,30,40,50,60,70]
p.line(listx2,listy2,line_width=5,legend="Female")
show(p)
