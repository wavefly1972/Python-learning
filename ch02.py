# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:42:17 2017

@author: 100419
"""

print("姓名  座號  國文  數學  英文")
print("%3s   %2d  %3d  %3d  %3d" % ("陳昭仁",1,100,100,100))

name=input("請輸入姓名:")
nat=input("請輸入國文成績:")
math=input("請輸入數學成績:")
eng=input("請輸入英文成績:")
sum=float(nat)+float(math)+float(eng)
average=sum/3
print("%s的成績總分: %5.2f , 平均成績: %5.2f" % (name,sum,average) )