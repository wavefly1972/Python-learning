# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:46:29 2017

@author: 100419
"""

import matplotlib.pyplot as plt

labels=["Japen","China","Taiwan","US"]
sizes=[1,2,3,4]
colors=["red","green","blue","yellow"]
explode=(0,0,0.0,0.1)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,startangle=60,pctdistance=0.6,labeldistance=1.1,autopct="%3.1f%%",shadow=True)
plt.axis("equal")
plt.legend()
plt.show()