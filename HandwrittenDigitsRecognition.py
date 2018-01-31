# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:43:19 2017

@author: 100419
"""

import numpy as np
from sklearn.datasets import load_digits #下載數據集
from sklearn.metrics import confusion_matrix, classification_report #用Matrix來表示有多少類是預測對，多少是錯的
from sklearn.preprocessing import LabelBinarizer #雖然有0~9十類，但在標記類別時只能用0,1表示，這是SKlearn的限制，當在表示自己的類別時，自已為1其它為0，所以是一個二維的數字類型
from NeuralNetwork1 import NeuralNetwork
from sklearn.cross_validation import train_test_split #分成K份，每K-1份當作訓練集，剩下一份做測試集，包含

digits=load_digits() #調用數據庫
X=digits.data #調用數據, 指的是特徵量
#print(X)
y=digits.target  #class label 0~9
#print(y)
X-=X.min() #normalize the value to bring them into the range 0-1
X/=X.max()
#print(X)

nn=NeuralNetwork([64,100,10],'Logistic')  #64個特徵值，10個class label,隱藏層比輸入大一點，可彈性
X_train, X_test, y_train, y_test=train_test_split(X,y)
#print(y_train)
labels_train=LabelBinarizer().fit_transform(y_train) #class label必須是0 or 1, 二進制化
labels_test=LabelBinarizer().fit_transform(y_test)
#print(y_test)
#print(labels_test)
print('start fitting')
nn.fit(X_train,labels_train,epochs=3000)
predictions=[]
for i in range(X_test.shape[0]):  #shape[0]有多少行
    o=nn.predict(X_test[i])
    #print(o)
    predictions.append(np.argmax(o))  #預測出來的值為零點幾，對應一個整數值，取最大值，對應的整數
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

#Confusion Matrix, 橫為真實值，縱為預測值
#classification_report, precision是所有為0的圖片，有98%確實都為0。recall是所有真實是0的圖片，有100%預測為0。