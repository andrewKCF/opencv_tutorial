#camera.py
import cv2
import numpy as np

cap = cv2.VideoCapture('http://192.168.23.31:5000/video_feed')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True: 
    ret, img = cap.read()
    cv2.imshow("Original", img)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()
