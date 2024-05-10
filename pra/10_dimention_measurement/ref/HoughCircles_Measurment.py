# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(title, image, destroy_all=True):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    if destroy_all:
        cv2.destroyAllWindows()
filepath='sample\sample0.jpg'
        
img = cv2.imread(filepath,0)
imgo=cv2.imread(filepath)
img = cv2.medianBlur(img,5)


#circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,300,param1=50,param2=30,minRadius=100,maxRadius=200)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,1000,param1=50,param2=30,minRadius=100,maxRadius=800)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
  cv2.circle(imgo,(i[0],i[1]),i[2],(255,0,0),2) # circle
  #print(i[2])
  cv2.circle(imgo,(i[0],i[1]),2,(255,0,0),12) # center point
  cv2.putText(imgo, "diameter:{:0.0f} pixel".format(i[2]*2), (i[0]-15, i[1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

show_image("Measurement Result",imgo, True)

