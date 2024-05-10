# TechVidvan Object detection of similar color

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)


while True:
    # Reading the image
    ret, img = cap.read()
    #define kernel size  
    kernel = np.ones((7,7),np.uint8)
    # convert to hsv colorspace 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower bound and upper bound
    lower_bound = np.array([9, 43, 117])     
    upper_bound = np.array([179, 139, 180])
    # find the colors within the boundaries
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    # Remove unnecessary noise from mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # Segment only the detected region
    segmented_img = cv2.bitwise_and(img, img, mask=mask)
    # Find contours from the mask
    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw contour on segmented image
    # output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)
    # Draw contour on original image
    output = cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
    # Showing the output
    # cv2.imshow("Image", img)
    cv2.imshow("Output", output)    
    #cv2.imshow('Video', img)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()  
