import cv2
import numpy as np

cap = cv2.VideoCapture('road_car_view.mp4')
while(True):
    ret,frame = cap.read()
    
    if ret:
        frame = cv2.resize(frame,(1500,800))
        blur = cv2.GaussianBlur(frame,(5,5),0)
        hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

        low_yellow = np.array([18,90,140])
        high_yellow = np.array([48,160,255])
        mask = cv2.inRange(hsv,low_yellow,high_yellow)
        canny = cv2.Canny(mask,50,150)
            
        roi_mask = np.zeros(canny.shape,dtype=np.uint8)
        ROI = np.array([[(0,800),(1400,800),(1400,350),(0,350)]])
        cv2.fillPoly(roi_mask,ROI,255)
        
        ROI_canny = cv2.bitwise_and(canny,roi_mask)        
        try:
            lines = cv2.HoughLinesP(ROI_canny,1,np.pi/180,50,maxLineGap=50,minLineLength=20)
            for line in lines:
                x1,y1,x2,y2 = line[0]
                cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),3)
        except:
            pass
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
