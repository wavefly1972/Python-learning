# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:56:43 2017

@author: 100419
"""

import numpy as np

def tanh(x):
    return np.tanh(x)

def tanh_deriv(x):
    return 1.0-np.tanh(x)*np.tanh(x) #微分

def logistic(x):
    return 1/(1+np.exp(-x))

def logistic_derivative(x):  #微分
    return logistic(x)*(1-logistic(x))

class NeuralNetwork: #定義類
    def __init__(self,layers,activation='tanh'): #__init__為創建構造函數，self指當前NeuralNetwork的類別
        #=====================================================
        #param layers:A list containing the number of units in each layer.Should be at least two values
        #param activiation: The activation function to be used. Can be "Logistic" or "tanh"
        ######
        
       if activation=='Logistic':
           self.activation = logistic
           self.activation_deriv=logistic_derivative
       elif activation == 'tanh':
           self.activation = tanh
           self.activation_deriv=tanh_deriv
        
       self.weights=[]  #List, 裝所有weight
       for i in range(1,len(layers)-1) : #1表示由第二層開始指定Weight, 向前和向後
           #k=np.random.random((3,3))
           #print(k)
           #print(layers[2])
           self.weights.append((2*np.random.random((layers[i-1]+1,layers[i]+1))-1)*0.25) #第二層和前面一層Weight assign,-0.25~0.25
           #print(self.weights)
           self.weights.append((2*np.random.random((layers[i]+1,layers[i+1]))-1)*0.25)   #第二層和後面一層weight assign
           #print(self.weights)
    #==================================================
    
    
    def fit(self,X,y,learning_rate=0.2,epochs=3):  #X數據集，y=class label,epochs:X用抽樣來訓練，不是全部拿來訓練，一次稱為1個epochs
        X=np.atleast_2d(X)  #確認X維度至少是2維的
        temp=np.ones([X.shape[0],X.shape[1]+1]) 
        #ones:全是1的距陣，shape:傳回X的維度值(行x列數)。shape[0]是行，shape[1]是列，+1是多一列(bias???)，此為對bias附值
        temp[:,0:-1]=X #行和X一樣，列從0到到數第2列 adding the bias unit to the input layer
        #print(temp)
        X=temp
        y=np.array(y)  #class label
        
        for k in range(epochs):
            i=np.random.randint(X.shape[0]) #從X中隨機取1行
            a=[X[i]] #放入a中準備訓練
            #print(a)
            #c=len(self.weights)
            #print(c)
            #print(self.weights)
            
            for l in range(len(self.weights)):  #going forward network, for each layer
                #kk=np.dot(a[l],self.weights[l]) #dot有含sum的功能
                #print(kk)
                a.append(self.activation(np.dot(a[l],self.weights[l]))) #Compute the node value. dot為相乖後SUM, activation就是非線性轉換
          #以上完成所有正向的Weight更新, a是正向走  
            #print(a[-1])
            #print(a)
            error=y[i]-a[-1]  #compute the error at the top(output) layer。a[-1]為output預測值
            deltas=[error*self.activation_deriv(a[-1])]  #Errj 輸出層誤差
            #print(deltas)
            #以下開始往回走 backpropagation
            
            for l in range(len(a)-2,0,-1):  #從Output往回一層，至第0層，-1為倒回去
            #We need to begin at the second to the last layers  
            #Compute the updated error(i.e,deltas) for each node going from
            
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l])) #deltas反向走，儲存隱藏層的更新
             #deltas存隱藏層更新後的誤差，乖以更新後的weight，再乘以Oj(1-Oj):梯度
            deltas.reverse()  #deltas 所有誤差
            
            for i in range(len(self.weights)):
                layer=np.atleast_2d(a[i])  #當前層，轉換成numpy array形式
                delta=np.atleast_2d(deltas[i]) #權重更新 delta W，每一層誤差
                self.weights[i] +=learning_rate*layer.T.dot(delta)
            
    def predict(self,x):
        x=np.array(x)
        temp=np.ones(x.shape[0]+1)
        temp[0:-1]=x
        a=temp
        for l in range(0,len(self.weights)):
            a=self.activation(np.dot(a,self.weights[l]))
        return a
    #print(a)
       
#nn=NeuralNetwork([2,2,1],'tanh')
#X=np.array([[0,0],[0,1],[1,0],[1,1]])
#print(X)
#z=np.array([0,1,1,0])
#nn.fit(X,z)
#for i in [[0,0],[0,1],[1,0],[1,1]]:
#    print(i,nn.predict(i))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    