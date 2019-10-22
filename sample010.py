import cv2 as cv
import numpy as np

def bi_image(image):
    dst = cv.bilateralFilter(image,0,50,15)#(圖片,半徑,顏色資訊,空間資訊)
    cv.imshow('bi_image',dst)

def mean_shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,0)
    cv.imshow('mean_shift_demo',dst)


print('------------------hello Python--------------------')
src = cv.imread("E:/PyAI/Image/bi_testImage.png")
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow('Input Image',src)
mean_shift_demo(src)
#bi_image(src)
cv.waitKey(0)
cv.destroyWindow('Input Image')