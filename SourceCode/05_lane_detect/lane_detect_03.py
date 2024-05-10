import cv2
import numpy as np
cap = cv2.VideoCapture('road_car_view.mp4')

while(True):
    ret,lane_img = cap.read()
    print (lane_img.shape)

    blur = cv2.GaussianBlur(lane_img,(5,5),0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    low_yellow = np.array([15,90,140])
    high_yellow = np.array([50,160,255])
    mask = cv2.inRange(hsv,low_yellow,high_yellow)

    canny = cv2.Canny(mask,50,150)


    lines = cv2.HoughLinesP(canny,1,np.pi/180,50,maxLineGap=50,minLineLength=20)

    for line in lines:
        x1,y1,x2,y2 = line[0]
        if (x1>640):
            print(640-x2);
            cv2.line(lane_img,(x1,y1),(x2,y2),(255,0,0),3)
            #cv2.circle(lane_img,(x1,y1), 10, (0, 0, 255), 3)
            cv2.circle(lane_img,(x2,y2), 10, (0, 255, 0), 3)
            break;


    # 文字
    text =  str(x1-640)

    # 使用各種字體
    cv2.putText(lane_img, text, (640, 360), cv2.FONT_HERSHEY_SIMPLEX,
      1, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.circle(lane_img,(640,720), 30, (0, 255, 255), 3)
    cv2.imshow('lane_img',lane_img)
    if cv2.waitKey(100) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
