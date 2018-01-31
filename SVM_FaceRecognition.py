# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 09:30:53 2017

@author: 100419
"""

from __future__ import print_function

from time import time  #步骤计时，，Ｔ
import logging #打印一些程序進展狀況
import matplotlib.pyplot as plt  #打印預測的人臉

from sklearn.cross_validation import train_test_split #
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC

print(__doc__)

#display progress logs on stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s') #程序中進展的信息打印出來

#=======================================================================
# Download the data, if not already on disk and load it as numpy arrays

lfw_people=fetch_lfw_people(min_faces_per_person=70,resize=0.4) #數據下載名人庫

# Introspect the images arrays to fine the shapes(for ploting)
n_samples, h, w = lfw_people.images.shape #返回 number of images
#print(h)
#print(w)
#print(n_samples)

# for machine learning we use the 2 data directly (as relative pixel
# positions info is ignored by this model)
X=lfw_people.data  #每一行是一個實例，每一列是個特徵向量
#print(X)
n_features = X.shape[1]  #每一個向量(圖,人臉)的維度，或number of 特徵值Shape[1]為列數


# the labe to predict is the id of the person
y=lfw_people.target #class label,對應的人臉
#print(y)
target_names=lfw_people.target_names #對應的人名
#print(target_names)
n_classes=target_names.shape[0]  #人名List中有多少行，即有多少人(類)要進行區分

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)

#=================================================================================
# Split into a training set and a test set using a stratified k fold
# split into a training and test set
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.25) 

#==============================================================================
#降data的維度
#Compute a PCA(eigenfaces) on the face dataset (treated as unlabeled dataset)
#: unuervised feature extrction/dimensionality reduction

n_components=150 #組成元素的數量

print("Extracting the top %d eigenfaces from %d faces" %(n_components, X_train.shape[0]))
t0=time()
#print(t0)
pca=RandomizedPCA(n_components=n_components,whiten=True).fit(X_train) #隨機隆維
print("done in %0.3fs" % (time()-t0))

eigenfaces=pca.components_.reshape((n_components,h,w))  #從人臉提取一些特徵點，叫做eigenface

print("Projecting te input data on the eigenfaces orthonormal basis")
t0=time()
#print(t0)
X_train_pca=pca.transform(X_train)  #針對X_train執行降維動作
X_test_pca=pca.transform(X_test)  #針對X_test執行降維動作
print("done in %0.3fs" %(time()-t0))
#===========================================================================================
# Train a SCM classification model

print("fitting the classifier to the training set")
t0=time()
param_grid ={'C':[1e3, 5e3, 1e4, 5e4, 1e5], 'gamma':[0.0001,0.0005,0.001,0.005,0.01,0.1],} #嚐試不同參數。共30種組合
# C:float,optional(default=1.0), Penalty parameter C of the error term 對錯誤進行懲罰，權重
# gamma:float, optional(default=0.0) Kernel coefficient for 'rbf", "poly" and "sigmoid"
# If gamma is 0.0 then 1/n_features will be used instead 多少特徵點會被使用將有一個比例

clf=GridSearchCV(SVC(kernel='rbf',class_weight='balanced'),param_grid) #GridSearchCV可試著不同組合
clf=clf.fit(X_train_pca, y_train)  #建模，找出使邊界條件最大的超平面。測試集根據超平面來分類
print("done in %0.3fs" % (time()-t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_) #打印出試出來的最好的Estimator的參數是多少
#===========================================================================================
#Quantitative evaluation of the model quality on the test set

print("Predicting people's names on the test set")
t0=time()
y_pred=clf.predict(X_test_pca)  #測試集分類預測
print("done in %0.3fs" % (time()-t0))

print(classification_report(y_test,y_pred,target_names=target_names))
print(confusion_matrix(y_test,y_pred,labels=range(n_classes))) #橫軸(行)為class label,縱軸為預測值
#==================================================================================
#Qualitative evaluation of the predictions using matplotlib 

def plot_gallery(images,titles,h,w,n_row=3,n_col=4):
    #====Helper fuction to plot a allaery of portraits
    plt.figure(figsize=(1.8*n_col,2.4*n_row))
    plt.subplots_adjust(bottom=0,left=0.1,right=.99,top=.90,hspace=.35)
    for i in range(n_row*n_col):
        plt.subplot(n_row,n_col, i+1)
        plt.imshow(images[i].reshape((h,w)),cmap=plt.cm.gray)
        plt.title(titles[i],size=12)
        plt.xticks(())
        plt.yticks(())
            
#=============================================================================
# plot the result of the prediction on a partion of the test set
        
def title(y_pred,y_test,target_names,i):
    pred_name=target_names[y_pred[i]].rsplit(' ',1)[-1]
    true_name=target_names[y_test[i]].rsplit(' ',1)[-1]
    #print('predicted: %s\ntrue:    %s' )
    return (pred_name,true_name)
    
prediction_titles=[title(y_pred,y_test,target_names,i) for i in range(y_pred.shape[0])]
plot_gallery(X_test, prediction_titles,h,w)

# plot the allery of the most significative eigenfaces

eigenface_titles=["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces,eigenface_titles,h,w)

plt.show()
                      
        












































