# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:03:42 2017

@author: 100419
"""

from sklearn.feature_extraction import DictVectorizer
import csv,array
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

#read in the csv file and put features in a list of dict and list of class label

allElectronicsData=open('C:\\SPB_Data\\temp\\ALLELectronics.csv','r')
#print(allElectronicsData)
reader=csv.reader(allElectronicsData)
#print(reader)
headers=reader.__next__()  #讀header
#print(headers)

featureList=[]
labelList=[]

#因sklearn不能處理"charactor"的資料，所以要將特徵值轉成"0"、"1"型式，以下皆為數值轉換
for row in reader:
    labelList.append(row[len(row)-1]) #取每一行最後的值(class label)加入labelList
    rowDict={} #用來取除了RID及class label外的特徵值
    for i in range(1,len(row)-1): #除了RID及class label皆取
        #print(row[i])
        #print(headers[i])
        rowDict[headers[i]]=row[i]  #以Dict方式儲存每一列特徵值
    featureList.append(rowDict)  #以list方式儲存所有特徵值, 值是Dict形式
print(featureList)


 #將特徵值轉成"0"、"1"型式
vec=DictVectorizer()

dummyX=vec.fit_transform(featureList).toarray() #
#dummyX=vec.fit_transform(featureList)
print("dummyX:" +str(dummyX))
print(vec.get_feature_names())
print("LabelList:"+str(labelList))    
        
#將class label轉成"0"、"1"型式
lb=preprocessing.LabelBinarizer()
dummyY=lb.fit_transform(labelList)
print("dummyY:"+str(dummyY))

#使用Python內建的decision tree classifier直接做分類
clf=tree.DecisionTreeClassifier(criterion='entropy') #使用ID3算法:信息熵
#print(str(clf))
clf=clf.fit(dummyX,dummyY) #建模
#print("clf:"+str(clf))  #看其它默認參數

#Visulize model
with open("aLLELectronicInformationGainOri.dot",'w') as f:
    f=tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f) #記得把feature name還原

#輸入測試數據進行測試
oneRowX=dummyX[0,:]
print("oneRowX:"+str(oneRowX))
newRowX=oneRowX
newRowX[0]=1
newRowX[2]=0
print("newRowX:"+str(newRowX))

#newnewRowX=[[newRowX]]
#print[str(newnewRowX)]
#newRowX.reshape(-1,1)

#print(str(newRowX))
array1=[[1,0,0,0,1,1,0,0,1,0]]
predictedY=clf.predict(array1)
#predictedY=clf.predict(newRowX)
print("predictedY:"+str(predictedY))








