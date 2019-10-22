import cv2 as cv
import numpy as np

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow('Gray',gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow('Hsv',hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow('Yuv',yuv)
    YCbCr = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow('YCbCr',YCbCr)



print('---------Hello Python -----------')
src = cv.imread('E:/PyAI/Image/Image1.jpg',)
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image",src)
color_space_demo(src)
cv.waitKey(0) #按0圖片檔會關掉
cv.destroyAllWindows()