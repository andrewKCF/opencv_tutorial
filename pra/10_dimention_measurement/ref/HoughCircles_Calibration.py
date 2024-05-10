# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
import mylib

filepath='photo1.jpg'

img_color=cv2.imread(filepath)        
img = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
img = cv2.medianBlur(img,5)
scale=80/628 #mm/pixel


#circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,300,param1=50,param2=30,minRadius=100,maxRadius=200)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,1000,param1=50,param2=30,minRadius=100,maxRadius=800)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
  cv2.circle(img_color,(i[0],i[1]),i[2],(255,0,0),2) # circle
  #print(i[2])
  cv2.circle(img_color,(i[0],i[1]),2,(255,0,0),12) # center point
  cv2.putText(img_color, "diameter:{:0.0f} pixel".format(i[2]*2), (i[0]-15, i[1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
  cv2.putText(img_color, "diameter:{:0.0f} mm".format(i[2]*2*scale), (i[0]-15, i[1]-40), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

mylib.show_image("Measurement Result",img_color, True)

