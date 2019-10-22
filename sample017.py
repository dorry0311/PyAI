import cv2 as cv
import numpy as np

def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_image = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_image.append(dst)
        cv.imshow('pyrmid_demo_'+str(i),dst)
        temp=dst.copy()


print("----------- Hello Python ------------")
src = cv.imread("E:/PyAI/Image/lena_color.jpg")  # 讀取圖檔
cv.imshow("Input Image",src)                        # 顯示圖片
cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)  # 自動調整視窗大小
pyramid_demo(src)
cv.waitKey(0)  # 等待使用者按按鍵
cv.destroyAllWindows()  # 關閉視窗