import cv2
import numpy as np
cap = cv2.VideoCapture(0)

logo= cv2.imread('hlbh.jpg')
cv2.imshow('logo',logo)
while True:
    #讀取兩張圖片
    ret,background = cap.read()

    y1,x1,ch1 = background.shape 
    y2,x2,ch2 = logo.shape #高度 寬度  

    #設定背景圖的ROI regiion
    roi = background[y1-y2:y1, x1-x2:x1]
    cv2.imshow('roi',roi)

    #轉成灰度圖
    gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

    #轉成二值化 logo mask
    ret, ma1 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
    cv2.imshow('ma1',ma1)
    fg1 = cv2.bitwise_and(roi,roi,mask=ma1)
    cv2.imshow('fg1',fg1)

    # logo inv mask
    ret, ma2 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('ma2',ma2)
    fg2 = cv2.bitwise_and(logo,logo,mask = ma2)
    cv2.imshow('fg2',fg2)

    # 影像相加
    roi[:] = cv2.add(fg1, fg2)
    cv2.imshow('roi2',roi)
    cv2.imshow('img1',background)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break;
# 释放VideoCapture
cap.release()
# 销毁所有的窗口
cv2.destroyAllWindows()
    
