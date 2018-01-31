# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:43:55 2017

@author: 100419
"""

import cv2,numpy
cv2.namedWindow("plot")
image=cv2.imread("media\\Jellyfish.jpg")
cv2.line(image,(50,50),(300,300),(250,0,0),2)
cv2.rectangle(image,(500,20),(580,100),(0,250,0),3)
cv2.rectangle(image,(100,300),(150,360),(0,0,250),-1)
cv2.circle(image,(500,300),40,(255,255,0),-1)
pts=numpy.array([[300,300],[300,340],[350,320]],numpy.int32)
cv2.polylines(image,[pts],True,(0,255,255),2)
cv2.putText(image,"Jellyfish.jpg",(350,420),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.imshow("plot",image)
cv2.waitKey(0)
cv2.destroyAllWindow()