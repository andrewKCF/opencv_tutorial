import cv2
import numpy as np
        
# 啟動攝影機（0 表示默認攝影機）
cap = cv2.VideoCapture(0)


while True:
    ret, img = cap.read()
    if not ret:
        break
    
    # 顯示影像
    cv2.imshow("Video", img)
    
    # 按下 'q' 鍵結束程式
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
# 釋放攝影機資源並關閉視窗
cap.release()
cv2.destroyAllWindows()
