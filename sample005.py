import cv2 as cv
import numpy as np

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)

def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)

def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow('divide_demo',dst)

def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1,m2)
    cv.imshow("logic_demo",dst)

def constrast_brightness_demo(image,c,b):#C為權重
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)#=image*c+blank*(1-c)+b<<偏移值
    cv.imshow('constrast_brightness_demo',dst)




print('---------Hello Python -----------')
src = cv.imread('E:/PyAI/Image/Image1.jpg')
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow('Input Image',src)
# src1 = cv.imread('E:/PyAI/Image/WIN.jpg')
# src2 = cv.imread('E:/PyAI/Image/LinuxLogo.jpg')
# print(src1.shape)
# print(src2.shape)
# cv.namedWindow('Input Image 1',cv.WINDOW_AUTOSIZE)
# cv.imshow('Input Image 1',src1)
# cv.namedWindow('Input Image 2',cv.WINDOW_AUTOSIZE)
# cv.imshow('Input Image 2',src2)
#subtract_demo(src1,src2)
#divide_demo(src1,src2)
#logic_demo(src1,src2)
constrast_brightness_demo(src,1.2,10)
cv.waitKey(0) #按0圖片檔會關掉
cv.destroyAllWindows()