import cv2 as cv
import numpy as np



src = cv.imread('E:/PyAI/Image/Image2.jpg')
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow('Input Image',src)
face = src[80:270,180:330]
cv.imshow('face image',face)
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)#單通道
backface = cv.cvtColor(gray,cv.COLOR_RGB2BGR)#COLOR_RGB2BGR是為了將gray轉為3通道
src[80:270,180:330] = backface
cv.imshow("face",src)

cv.waitKey(0) #按0圖片檔會關掉
cv.destroyAllWindows()