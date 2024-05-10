#capture
import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
i = 0

while True:
    ret, img = cap.read()
    cv2.imshow('Video', img)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break;
    if key==ord('s'):
        i = i + 1
        cv2.imwrite('photo' + str(i) + '.jpg',img)
        print('save','photo' + str(i) + '.jpg')

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
