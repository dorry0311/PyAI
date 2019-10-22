import cv2 as cv
import numpy as np

def extract_hair(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow('HSV',hsv)
    low_hsv = np.array([0,0,0])
    high_hsv = np.array([180,255,46])
    dst = cv.inRange(hsv,low_hsv,high_hsv)
    cv.imshow("result",dst)

def extrace_object_demo():#擷取攝像中的某顏色
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        frame = cv.flip(frame,1)#1=水平反轉 0上下反轉 -1水平垂直皆反轉
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        low_hsv = np.array([35, 43, 46])#最小值的HSV
        high_hsv = np.array([77, 255, 255])#
        dst = cv.inRange(hsv,low_hsv,high_hsv)
        cv.imshow("mask",dst)
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c == 27:
            break



print('---------Hello Python -----------')
src = cv.imread('E:/PyAI/Image/Image1.jpg',)
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow('input image',src)
extract_hair(src)
extrace_object_demo()
b, g, r = cv.split(src)                              # 將影像通道分離
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
src1 = cv.merge([b,g,r])
cv.imshow("src1",src1)
cv.waitKey(0) #按0圖片檔會關掉
cv.destroyAllWindows()
