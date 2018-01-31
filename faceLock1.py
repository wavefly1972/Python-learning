# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:13:46 2017

@author: 100419
"""
import cv2,os,math,operator
from PIL import Image
from functools import reduce



def makeFace(facename,msg,endstr):
    print(msg)  #顯示提示訊息
    cv2.namedWindow("frame")
    cv2.waitKey(0)
    cap=cv2.VideoCapture(0)
    while(cap.isOpened()): #攝像機開啟偵測
       ret,img=cap.read()
       if ret == True:
          cv2.imshow("frame",img)
          k=cv2.waitKey(100)       #每0.1秒讀一次
          if k==ord("z") or k==ord("Z"):
             cv2.imwrite(facename,img)  #存檔
             image=cv2.imread(facename)  #讀檔作臉部辨識
             faces=faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
             
             (x,y,w,h)=(faces[0][0],faces[0][1],faces[0][2],faces[0][3])  #只取第一張臉譜
             image1=Image.open(facename).crop((x,y,x+w,y+h))  #擷取臉部
             image1=image1.resize((200,200),Image.ANTIALIAS)
             image1.save(facename)
             print(endstr)
             break 
    cap.release()    #關閉攝影機
    cv2.waitKey(5000)
    cv2.destroyWindow("frame")
    

#casc_path="C:\\Anaconda3\\pkgs\\opencv3-3.1.0-py35_0\\Library\etc\\haarcascades\\haarcascade_frontalface_defaul.xml"
#faceCascade=cv2.CascadeClassifier(casc_path)
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #建立辨識物件

recogname="C:\\SPB_Data\\media\\recogface.jpg" #使用者臉部檔案
loginname="C:\\SPB_Data\\media\\loginface.jpg"  #登入者臉部檔案
os.system("cls")  #清除螢幕
if(os.path.exists(recogname)):  #如果使用者臉部檔案已存在
    msg="按任意鍵建立登入者臉譜。 \n 攝影機開啟後按[Z]拍照比對! "
    makeFace(loginname,msg,"") #建立登入者臉部檔案
    pic1=Image.open(recogname)  #開啟使用者臉部檔案
    pic2=Image.open(loginname)  #開啟登入者臉部檔案
    h1=pic1.histogram()  #計算圖形差異度
    h2=pic2.histogram()
    diff=math.sqrt(reduce(operator.add,list(map(lambda a,b:(a-b)**2,h1,h2)))/len(h1))
    if(diff<=100):  #若差度在100內視為通過驗証
        print("通過驗証，歡迎使用本系統! diff=%4.2f " %diff)
    else:
        print("臉譜不正確，無法使用本系統! diff=%4.2f" %diff )
else:
    msg="按任意鍵建立使用者臉譜。 \n 攝影機開啟後按[Z]拍照! \n"
    endstr="使用者臉譜建立完成!"
    makeFace(recogname,msg,endstr)  #建立使用者檔案





     