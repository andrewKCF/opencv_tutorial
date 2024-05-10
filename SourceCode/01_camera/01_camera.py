#camera.py
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True: 
    ret, img = cap.read()
    cv2.imshow("Video", img) 
    key=cv2.waitKey(1)
    if key==ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()
