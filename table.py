# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:39:12 2017

@author: 100419
"""

import pandas as pd
tables=pd.read_html("http://www.stockq.org/market/commodity.php")
#n=1
#for table in tables:
#    print("第"+str(n)+"個表格:")
#    print(table.head())
#    print()
#    n+=1
table=tables[7]
table=table.drop(table.index[[0,1]])
table.columns=["商品","買價","漲跌","比例","台北"]
table.index=range(len(table.index))
print(table)