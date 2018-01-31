# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:29:21 2017

@author: 100419
"""

import cv2
casc_path="C:\\Anaconda3\\pkgs\\opencv3-3.1.0-py35_0\\Library\etc\\haarcascades\\haarcascade_frontalface_defaul.xml"
#faceCascade=cv2.CascadeClassifier(casc_path)
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#cv2.namedWindow("plot")
#imagename=cv2.imread("C:\\SPB_Data\\media\\Allan.jpg")
#cv2.imshow("plot",imagename)
#cv2.waitKey(0)
#cv2.destroyAllWindow()
imagename=cv2.imread("C:\\SPB_Data\\media\\Allan3.jpg")
faces=faceCascade.detectMultiScale(imagename, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
imagename.shape[0] #圖片高度
imagename.shape[1] #圖片寬度
cv2.rectangle(imagename,(10,imagename.shape[0]-20),(110,imagename.shape[0]),(0,0,0),-1)
cv2.putText(imagename,"Find"+str(len(faces))+"face!",(10,imagename.shape[0]-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
for (x,y,w,h) in faces:
    cv2.rectangle(imagename,(x,y),(x+w,y+h),(128,255,0),2)
cv2.namedWindow("facedetect")
cv2.imshow("facedetect",imagename)
cv2.waitKey(0)
cv2.destroyWidndow("facedetect")