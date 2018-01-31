# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:09:37 2017

@author: 100419
"""

import matplotlib.pyplot as plt

plt.xlim(2016,2028)
plt.ylim(200,2000)
listx1=[2017,2018,2019,2020,2021,2022]
listy1=[280,380,580,780,1000,1200]
#plt.plot(listx,listy)
plt.plot(listx1,listy1,color="red",linestyle="--",label="Salary1",lw=5.0)


plt.xlim(2013,2024)
plt.ylim(100,2000)
listx2=[2017,2018,2019,2020,2021,2022]
listy2=[380,680,780,980,1100,1500]
plt.bar(listx2,listy2,color="blue",label="Salary2")

plt.title("Salary each year")
plt.xlabel("year")
plt.ylabel("MNTD")

plt.legend()
plt.show()