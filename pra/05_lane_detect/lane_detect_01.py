import cv2
import numpy as np

img = cv2.imread('lines.jpg',-1)
cv2.imshow('line',img)
print(img.shape)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
canny = cv2.Canny(img,50,150)
cv2.imshow('draw_line',canny)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
canny = cv2.Canny(img,50,150)

lines = cv2.HoughLinesP(canny,1,np.pi/180,50,maxLineGap=180,minLineLength=20)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
    
cv2.imshow('draw_line',img)
