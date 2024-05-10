import cv2
import numpy as np
cap = cv2.VideoCapture(0)

logo= cv2.imread('hlbh.jpg')
cv2.imshow('logo',logo)
while True:
    cv2.imshow('img1',background)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break;
# 释放VideoCapture
cap.release()
# 销毁所有的窗口
cv2.destroyAllWindows()
    
