# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:11:03 2017

@author: 100419
"""

import glob
files=glob.glob("gob.py")+glob.glob("os*.py")+glob.glob("*.txt")
for file in files:print(file)