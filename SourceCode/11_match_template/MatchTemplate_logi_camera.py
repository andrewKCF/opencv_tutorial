import cv2
import numpy as np
from matplotlib import pyplot as plt
import mylib

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
i = 0;

while True:
    ret, img = cap.read()
    cv2.imshow('Video', img)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break;

img_bgr = img
template = cv2.imread('logo1.jpg',0)
th, tw = template.shape[::]

img = img_bgr
img = mylib.noise_reduction(img)
mylib.show_image("noise reduction",img, True)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mylib.show_image("gray",img, True)


ret,img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
mylib.show_image("binary",img, True)

rv = cv2.matchTemplate(img,template,3)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

topLeft = minLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img_bgr,topLeft, bottomRight, (0,0,255), 4) # min 

topLeft = maxLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img_bgr,topLeft, bottomRight, (255,0,0), 4) # max

print('minVal(Red):',minVal)
print('maxVal(Blue):',maxVal)

plt.subplot(121),plt.imshow(mylib.rgb(template))
plt.title('Matching Template'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(mylib.rgb(img_bgr))
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
