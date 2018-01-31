# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:23:43 2017

@author: 100419
"""

from bokeh.plotting import figure,show
p=figure(width=800,height=400,title="Statistics Diagram")
listx=[1,5,7,13,16]
listy=[15,30,50,60,80,90]
p.line(listx,listy)
show(p)
