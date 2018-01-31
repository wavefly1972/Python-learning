# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:12:09 2017

@author: 100419
"""

print(__doc__)

import numpy as np #矩阵计算
import pylab as pl #画图
from sklearn import svm

#we create 40 separable points

np.random.seed(0)   #參數0表示每次重啟40組亂數保持一樣
X=np.r_[np.random.randn(20,2)-[2,2], np.random.randn(20,2)+[2,2]] #randn為產生高斯分布，mean為0,deviation為1 or 2?? [2,2]是offset, 表示均值是2，方差也是2
#print(X)
Y=[0]*20+[1]*20
#print(Y)

#fit the model
clf=svm.SVC(kernel='linear')
clf.fit(X,Y)

#get the separating hyperplane. w0x+w1y+intercept=0 => y=(-w0/w1)x-intercept/w1
w=clf.coef_[0]  #取得w0,w1
print('w:',w)
a=-w[0]/w[1]
print('a:',a)
xx=np.linspace(-5,5,50)  #從-5到5產生50組連續x值 -5,-4...要代進去公式得到Hyperplane上的Y值
#print(xx)
#bb=clf.intercept_[0]
#print('bb:',bb)
yy=a*xx-(clf.intercept_[0]/w[1])#print(yy)

#plot the parallels to the separating hyperplane that pass thrugh the support vector
#和support vector相切的Hyperplane斜率和Hyperplane一樣，只是intercept值不一樣
print(clf.support_vectors_)
print(clf.support_)
print(clf.n_support_)
b=clf.support_vectors_[0]
print('b:',b)
yy_down=a*xx+(b[1]-a*b[0])  #  b[0]、b[1]代入y=ax+intercept_down, b[1]=a*b[0]+intercept_down
c=clf.support_vectors_[-1]  #最后一個Support vector是在Hyperplane上方
yy_up=a*xx+(c[1]-a*c[0])

#switching to the generic n-dimensional parameterization of the hyperplane to the 2D specific equiation of  a line y=ax+b: the generic w0x+w1y+w3=0 can be rewritten y=-(w0/w1)x+(w3/w1)

#plot the line, the points, and the nearest vectors to the plane
pl.plot(xx,yy,'k-')
pl.plot(xx,yy_down,'k--')
pl.plot(xx,yy_up,'k--')
print(clf.support_vectors_[:,0])
pl.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],s=100,facecolors='red') #標出support vector
pl.scatter(X[:,0],X[:,1],c=Y, cmap=pl.cm.Paired)
pl.axis('tight')
pl.show()

