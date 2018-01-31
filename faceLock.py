# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:33:45 2017

@author: 100419
"""

import cv2
cv2.namedWindow("frame")
cap=cv2.VideoCapture(0)
while(cap.isOpened()): #攝像機開啟偵測
    ret,img=cap.read()
    if ret == True:
        cv2.imshow("frame",img)
        k=cv2.waitKey(100)
        if k==ord("z") or k==ord("Z"):
            cv2.imwrite("C:\\SPB_Data\\media\\catch.jpg",img)
            break

cap.release()
cv2.waitKey(0)
cv2.destroyWindow("frame")