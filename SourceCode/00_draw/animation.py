import cv2 
import numpy as np
img=np.zeros((500, 500, 3), dtype=np.uint8)
img.fill(255)
while True: 
    for i in range(200,0,-20): 
        #print(i)
        r=np.random.randint(3,high=18)
        print(r)
        cv2.circle(img, (250, 250), i, (0, 0, 0), r)       
        
    cv2.imshow('draw', img)
    cv2.waitKey(1000)
    img.fill(255)   
