# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 17:38:09 2017

@author: 100419
"""

def calsum(*params):
    total=0
    for param in params:
        total+=param
    return total
print("不定數目範例：")
print("2個參數:calsum(4,5,12,11)=%d" % calsum(4,5,12,11))