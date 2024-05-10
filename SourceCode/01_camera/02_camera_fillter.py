#camera.py
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True: 
    ret, img = cap.read()
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.blur(img,(10,10))
    #img = cv2.GaussianBlur(img,(7,7),0,0)
    #img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
   
    ret, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    img = cv2.Canny(img,100,200)
    cv2.imshow("Video", img) 

    key=cv2.waitKey(1)
    if key==ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()
