import cv2 
import numpy as np
img=np.zeros((500, 500, 3), dtype=np.uint8)
img.fill(255)
x=250
y=250
rad=60
cv2.circle(img, (x-rad, y-rad), rad, (0,0,255), -1)
cv2.circle(img, (x+rad, y-rad), rad,(0,0,255),-1)
cv2.circle(img, (x-rad, y+rad), rad, (0,0,255),-1)
cv2.circle(img, (x+rad, y+rad), rad, (0,0,255), -1)
cv2.circle(img, (x, y), rad, ( 215,0 ,255), -1)
cv2.imshow('draw', img)
