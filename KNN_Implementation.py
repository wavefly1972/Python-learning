# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:03:15 2017

@author: 100419
"""

import csv
import random
import math
import operator

def loadDataset(filename,split,trainingSet=[],testSet=[]):
    with open(filename,'rt') as csvfile:
        lines=csv.reader(csvfile)
        #print(lines)
        dataset=list(lines)  #所有資料變List
        #print(dataset)
        #b=len(dataset)
        #print(b)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y]=float(dataset[x][y])
                #print(dataset[0][4])
            if random.random()<split:
                trainingSet.append(dataset[x])
                #print(trainingSet)
            else:
                testSet.append(dataset[x])
    #print(dataset[0][4])

                
def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)
    
def getNeighbors(trainingSet,testInstance,k):
    distances=[]
    length=len(testInstance)-1
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes={}  #dict
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response]=1
            
    sortedVotes=sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet,predictions):
    correct=0
    #a=len(testSet)
    #print(a)
    for x in range(len(testSet)):
        #print(testSet[x][-1])
        #print(predictions[x])
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return(correct/float(len(testSet))) * 100.0
    
def main():
    #prepare data
    trainingSet=[]
    testSet=[]
    split=0.67
    loadDataset('C:\\SPB_Data\\temp\\Irisdata.csv',split,trainingSet,testSet)
    print("Train set:" + repr(len(trainingSet)))
    print("Test set:" + repr(len(testSet)))
    #generate predictions
    predictions=[]
    k=3
    #print(testSet[1][-1])
    for x in range(len(testSet)):
        print(testSet[x])
        neighbors=getNeighbors(trainingSet,testSet[x],k) #一次拿testSet的一個元素去計算KNN
        result=getResponse(neighbors)
        predictions.append(result)
        #print(predictions)
        #b=len(predictions)
        #print(b)
        #print('>predicted=' + repr(result) +',actual=' + repr(testSet[x][-1]))
        #print(testSet)
    accuracy=getAccuracy(testSet,predictions)
    print('Accuracy:' +repr(accuracy) + '%')

main()
    
    
    
    
    
    
    
    
    
    
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
                
                
                
                