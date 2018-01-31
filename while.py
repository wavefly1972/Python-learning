# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:39:54 2017

@author: 100419
"""

total=person=score=0
while(score!=-1):
    person += 1
    total += score
    score=int(input("請輸入第 %d 位學生的成績:" % person))
average=float(total/(person-1))
print("本班總成績:%d 分，平均成績：%5.2f 分" % (total,average))