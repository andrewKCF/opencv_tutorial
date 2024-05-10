# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_image(title, image, destroy_all=True):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    if destroy_all:
        cv2.destroyAllWindows()

img_file='photo1.jpg'
template_file='logo1.jpg'

img = cv2.imread(img_file,0)
img_bgr = cv2.imread(img_file)

#t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#show_image("Measurement Result",rst, True)

template = cv2.imread(template_file,0)

th, tw = template.shape[::]

rv = cv2.matchTemplate(img,template,3)
#cv2.TM_SQDIFF
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
print('minVal:',minVal)
print('maxVal:',maxVal)
topLeft = minLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img_bgr,topLeft, bottomRight, (0,0,255), 4)

topLeft = maxLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img_bgr,topLeft, bottomRight, (255,0,0), 4)

img_rgb = img_bgr[:,:,::-1]



plt.subplot(121),plt.imshow(template,cmap = 'gray')
plt.title('Matching Template'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.subplot(122),plt.imshow(img_rgb)
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
