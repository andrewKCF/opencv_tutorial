import cv2 
import numpy as np
img=np.zeros((500, 500, 3), dtype=np.uint8)
img.fill(255)
x=250
y=250
rad=60

while True:
    x=np.random.randint(0,high=500)
    y=np.random.randint(0,high=500)
    
    r=np.random.randint(0,high=255)
    g=np.random.randint(0,high=255)
    b=np.random.randint(0,high=255)
    
    cv2.circle(img, (x-rad, y-rad), rad, (b,g,r), -1)
    r=np.random.randint(0,high=255)
    g=np.random.randint(0,high=255)
    b=np.random.randint(0,high=255)    
    cv2.circle(img, (x+rad, y-rad), rad,(b,g,r),-1)
    r=np.random.randint(0,high=255)
    g=np.random.randint(0,high=255)
    b=np.random.randint(0,high=255)     
    cv2.circle(img, (x-rad, y+rad), rad, (b,g,r),-1)
    r=np.random.randint(0,high=255)
    g=np.random.randint(0,high=255)
    b=np.random.randint(0,high=255)     
    cv2.circle(img, (x+rad, y+rad), rad, (b,g,r), -1)
    cv2.circle(img, (x, y), rad, ( 215,0 ,255), -1)
    cv2.imshow('draw', img)

        
    cv2.imshow('draw', img)
    key = cv2.waitKey(1000)
    if key == ord('q'):
        break
    img.fill(255)
cv2.destroyAllWindows()    
