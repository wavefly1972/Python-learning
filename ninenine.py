# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:50:38 2017

@author: 100419
"""

for i in range(1,10):
    for j in range(1,10):
        product=i*j
        print("%d*%d=%-2d " % (i,j,product), end="")
    print()