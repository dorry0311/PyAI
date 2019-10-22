import cv2 as cv
import numpy as np


# def video_demo():
#     capture = cv.VideoCapture(0)
#     while(True):
#         ret, frame = capture.read()
#         frame = cv.flip(frame,1)
#         #1=水平反轉 0上下反轉 -1水平垂直皆反轉
#         cv.imshow('video',frame)
#         c = cv.waitKey(50)
#         if c == 27: #27為ESC鍵
#             break

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

print('---------Hello Python -----------')
src = cv.imread('E:/PyAI/Image/harry.jpg',)
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image",src)
get_image_info(src)
#video_demo()
cv.waitKey(0) #按0圖片檔會關掉
cv.destroyAllWindows()
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite('E:/PyAI/Image/harry.jpg',gray)