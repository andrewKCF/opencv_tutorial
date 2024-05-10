import cv2
from cspaceSliders import FilterWindow


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    ret, img = cap.read()
    cv2.imshow('Video', img)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        cv2.imwrite('photo.jpg',img)
        break

cap.release()
cv2.destroyAllWindows()        



window = FilterWindow('Filter Window', img)
window.show(verbose=True)

colorspace = window.colorspace
lowerb, upperb = window.bounds
mask = window.mask
applied_mask = window.applied_mask

print('Displaying the image with applied mask filtered in', colorspace,
      '\nwith lower bound', lowerb, 'and upper bound', upperb)
cv2.imshow('Applied Mask', applied_mask)
cv2.waitKey()
