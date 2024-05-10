#06_face_detect
import cv2
smile= cv2.imread('smil_face.png')
sh,sw=smile.shape[:2]
print (sw) # width
print (sh) # heigh


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('face01.jpg')


# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    print (w)
    print (h)
    scale_w=w/sw
    scale_h=h/sh
    smile_rz=cv2.resize(smile,None,fx=scale_w,fy=scale_h)
    cv2.imshow('resize', smile_rz)
    roi=img[y:y+h,x:x+w]
    roi[:,:,0]=0 # blue
    roi[:,:,1]=0 # green
    roi[:,:,2]=0 # red
    cv2.imshow('roi', roi)
    roi[:]=cv2.add(roi,smile_rz)
    cv2.imshow('img', img)
    cv2.waitKey(1)
    
# Display the output
#cv2.imshow('img', img)
#cv2.waitKey()
