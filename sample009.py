import cv2 as cv
import numpy as np

def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv
def gaussian_noise(image):
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            b = image[row,col,0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row,col,0] = clamp(b+s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("gaussian_noise",image)


print('------------------hello Python--------------------')
src = cv.imread("E:/PyAI/Image/Image1.jpg")
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow('Input Image',src)
gaussian_noise(src)
cv.waitKey(0)
cv.destroyAllWindows('Input Image')