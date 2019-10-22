import cv2 as cv
import numpy as np

def fill_color_demo(image):
    copyimage = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    (b,g,r) = copyimage[455,250]
    print("位置(250,455)處的像素 -紅:%d,綠:%d,藍:%d"%(r,g,b))
    cv.floodFill(copyimage,mask,(250,455),(0,0,255),(50,30,30),(100,100,100),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyimage)

def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("fill_binary",image)
    mask = np.ones([400 + 2,400 + 2],np.uint8)
    mask[99:301,99:301]=0
    cv.floodFill(image,mask,(200,200),(0,255,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow('fill_binary',image)

print('---------Hello Python -----------')
src = cv.imread('E:/PyAI/Image/Image1.jpg')
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow('Input Image',src)
#fill_color_demo(src)
fill_binary()
cv.waitKey(0) #按0圖片檔會關掉

cv.destroyAllWindows()