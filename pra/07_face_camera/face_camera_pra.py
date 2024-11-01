'''
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
'''
import cv2

# Load the cascade
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) 

while True: 
    ret, img = cap.read()

    cv2.imshow("Video", img) 
    key=cv2.waitKey(1)
    if key==ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()
