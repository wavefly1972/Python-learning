# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:15:23 2017

@author: 100419
"""

from sklearn import tree
import numpy as np
features =[[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]
labels = np.array(labels).reshape(1,-1)
print(labels)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
#print clf.predict([150,0])