import cv2 
import numpy as np
img=np.zeros((500, 500, 3), dtype=np.uint8)
img.fill(255)
for i in range(200,0,-20): 
    print(i) 
    cv2.circle(img, (250, 250), i, (0, 0, 0), 7)


cv2.imshow('draw', img) 
