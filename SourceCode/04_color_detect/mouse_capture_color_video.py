import cv2
import numpy as np
r=0
g=0
b=0
# 定義回調函數，在滑鼠移動時取得 RGB 值
def get_rgb(event, x, y, flags, param):
    global r,g,b
    if event == cv2.EVENT_MOUSEMOVE:  # 當滑鼠移動時
        # 取得該點的 RGB 值
        b, g, r = img[y, x]
        print(f"RGB值: R={r}, G={g}, B={b}")
        
# 啟動攝影機（0 表示默認攝影機）
cap = cv2.VideoCapture(0)

# 設定滑鼠事件回調
cv2.namedWindow("Video")
cv2.setMouseCallback("Video", get_rgb)

while True:
    ret, img = cap.read()
    if not ret:
        break
    # lower bound and upper bound
    lower_bound = np.array([b-10, g-10, r-10])     
    upper_bound = np.array([b+10, g+10, r+10])
    # find the colors within the boundaries
    mask = cv2.inRange(img, lower_bound, upper_bound)
    
    # 顯示影像
    cv2.imshow("Video", img)
    cv2.imshow("Mase", mask)
    
    # 按下 'q' 鍵結束程式
    key=cv2.waitKey(1)
    if key == ord('q'):
        break

# 釋放攝影機資源並關閉視窗
cap.release()
cv2.destroyAllWindows()
