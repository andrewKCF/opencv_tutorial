import cv2 as cv
import numpy as np
from urllib.request import urlopen
import os
import datetime
import time
import sys

# Load the cascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#change to your ESP32-CAM ip
url="http://192.168.4.116:81/stream"   
CAMERA_BUFFRER_SIZE=4096
stream=urlopen(url)
bts=b''
i=0
while True:    
    try:
        bts+=stream.read(CAMERA_BUFFRER_SIZE)
        jpghead=bts.find(b'\xff\xd8')
        jpgend=bts.find(b'\xff\xd9')
        if jpghead>-1 and jpgend>-1:
            jpg=bts[jpghead:jpgend+2]
            bts=bts[jpgend+2:]
            img=cv.imdecode(np.frombuffer(jpg,dtype=np.uint8),cv.IMREAD_UNCHANGED)
            #img=cv.flip(img,0) #>0:垂直翻轉, 0:水平翻轉, <0:垂直水平翻轉            
            #h,w=img.shape[:2]
            #print('影像大小 高:' + str(h) + '寬：' + str(w))
            img=cv.resize(img,(640,480))

            # Convert into grayscale
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            

            # Draw rectangle around the faces
            for (x, y, w, h) in faces:
                cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            
            cv.imshow("a",img)
        k=cv.waitKey(1)
    except Exception as e:
        print("Error:" + str(e))
        bts=b''
        stream=urlopen(url)
        continue
    
    k=cv.waitKey(1)
    # 按a拍照存檔
    if k & 0xFF == ord('a'):
        cv.imwrite(str(i) + ".jpg", img)
        i=i+1
    # 按q離開
    if k & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
