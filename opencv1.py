# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:51:54 2017

@author: 100419
"""

import cv2
cv2.namedWindow("ShowImage1")
cv2.namedWindow("ShowImage2")
image1=cv2.imread("media\\Jellyfish.jpg")
image2=cv2.imread("media\\Jellyfish.jpg",-1)
#image2=cv2.imread("media\\Jellyfish.jpg",1)
cv2.imshow("ShowImage1",image1)
cv2.imshow("ShowImage2",image2)
cv2.waitKey(10000)
cv2.destroyAllWindows()