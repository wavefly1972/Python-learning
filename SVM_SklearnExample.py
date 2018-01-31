# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:57:15 2017

@author: 100419
"""

from sklearn import svm
x=[[2,0],[1,1],[2,3]]
y=[0,0,1]  #Class label
clf=svm.SVC(kernel='linear') #分类器
clf.fit(x,y)  #带入预测值
print(clf)

##get support vectors
print(clf.support_vectors_)
#a=clf.support_vectors_
#print(a)

#get indices of support vectors
print(clf.support_)

#get number of support vectors for each class
print(clf.n_support_)