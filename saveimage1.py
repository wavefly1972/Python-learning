# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:05:45 2017

@author: 100419
"""

import cv2
cv2.namedWindow("ShowImage")
image=cv2.imread("media\\Jellyfish.jpg",0)
cv2.imshow("ShowImage",image)
cv2.imwrite("media\\Jellyfishcopy1.jpg",image)

cv2.imwrite("media\\Jellyfishcopy2.jpg",image,[int(cv2.IMWRITE_JPEG_QUALITY),50])
cv2.waitKey(0)
cv2.destroyWindow("ShowImage")