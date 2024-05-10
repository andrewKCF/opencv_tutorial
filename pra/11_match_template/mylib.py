import cv2
import numpy as np
from matplotlib import pyplot as plt
def show_image(title, image, destroy_all=True):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    if destroy_all:
        cv2.destroyAllWindows()

def noise_reduction(img):
    import numpy as np
    import cv2
    from matplotlib import pyplot as plt

    b,g,r = cv2.split(img)           # get b,g,r
    rgb_img = cv2.merge([r,g,b])     # switch it to rgb

    # Denoising
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

    b,g,r = cv2.split(dst)           # get b,g,r
    rgb_dst = cv2.merge([r,g,b])     # switch it to rgb

    plt.subplot(121),plt.imshow(rgb_img)
    plt.subplot(122),plt.imshow(rgb_dst)
    plt.show()
    return dst
def rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
