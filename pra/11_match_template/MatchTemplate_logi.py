import cv2
import numpy as np
from matplotlib import pyplot as plt
import mylib

img_file='photo1.jpg'
template_file='logo3.jpg'

img_bgr = cv2.imread(img_file)
template = cv2.imread(template_file,0)
th, tw = template.shape[::]

img = img_bgr
img = mylib.noise_reduction(img)
mylib.show_image("noise reduction",img, True)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mylib.show_image("gray",img, True)

ret,img=cv2.threshold(img,110,255,cv2.THRESH_BINARY)
mylib.show_image("binary",img, True)

#cv2.TM_SQDIFF
#cv2.TM_SQDIFF_NORMED
#cv2.TM_CCORR
#cv2.TM_CCORR_NORMED
#cv2.CV_TM_CCOEFF
#cv2.CV_TM_CCOEFF_NORMED

rv = cv2.matchTemplate(img,template,cv2.TM_SQDIFF) 
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

topLeft = minLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img_bgr,topLeft, bottomRight, (0,0,255), 4) # min 

topLeft = maxLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img_bgr,topLeft, bottomRight, (255,0,0), 4) # max

print('minVal(Red) :',minVal)
print('maxVal(Blue):',maxVal)

plt.subplot(121),plt.imshow(mylib.rgb(template))
plt.title('Matching Template'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(mylib.rgb(img_bgr))
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
