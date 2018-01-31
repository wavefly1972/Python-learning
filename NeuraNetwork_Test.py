# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:59:33 2017

@author: 100419
"""

from NeuralNetwork1 import NeuralNetwork
import numpy as np

nn=NeuralNetwork([2,2,1],'tanh')
X=np.array([[0,0],[0,1],[1,0],[1,1]])
#print(X)
y=np.array([0,1,1,0])
nn.fit(X,y)
for i in [[0,0],[0,1],[1,0],[1,1]]:
    print(i,nn.predict(i))

