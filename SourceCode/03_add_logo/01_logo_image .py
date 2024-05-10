import cv2
import numpy as np
background = cv2.imread('02.jpg')
logo= cv2.imread('ettc.jpg')


#讀取兩張圖片
r1,c1,ch1 = background.shape 
r2,c2,ch2 = logo.shape #高度 寬度  

#設定背景圖的ROI regiion
roi = background[r1-r2:r1, c1-c2:c1]


#轉成灰度圖
gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

#轉成二值化 logo mask
ret, ma1 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
fg1 = cv2.bitwise_and(roi,roi,mask=ma1)



# logo inv mask
ret, ma2 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)
fg2 = cv2.bitwise_and(logo,logo,mask = ma2)

# 影像相加
roi[:] = cv2.add(fg1, fg2)

cv2.imshow('img1',background)
cv2.waitKey(0)
cv2.destroyAllWindows()
