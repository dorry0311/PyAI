import cv2 as cv
import numpy as np

def equalHist_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo",dst)

def clahe_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst = clahe.apply(gray)
    cv.imshow('clahe_demo',dst)


print('------------------hello Python--------------------')
src = cv.imread("E:/PyAI/Image/HistTest.jpg")
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow('Input Image',src)
equalHist_demo(src)
clahe_demo(src)
cv.waitKey(0)
cv.destroyWindow('Input Image')