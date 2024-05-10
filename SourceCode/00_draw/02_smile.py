import cv2 
import numpy as np
img=np.zeros((500, 500, 3), dtype=np.uint8)
img.fill(255)
cv2.circle(img, (250, 250), 200, (0, 0, 0), 2)
cv2.circle(img, (150, 150), 50, (0, 0, 0), 2)
cv2.circle(img, (350, 150), 50, (0, 0, 0), 2)
cv2.ellipse(img,(250, 350), (100, 50), 0, 0, 180, (44, 141, 108), 2)
cv2.imshow('draw', img) 
