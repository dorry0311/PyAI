import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    print('height : %s,widht : %s,channel : %s'%(height,width,channel))
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow('access_pixels',image)

def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("imverse",dst)


def create_image():#製造影像
    # m1 = np.ones([3,3],np.float32)
    # m1.fill(123.456)
    # print(m1)
    # m2 = m1.reshape([1,9])
    # print(m2)


    img = np.zeros([400,400,3],np.uint8)#設計影像大小[高,寬,3通道]
    img[:,:,2] = np.ones([400,400])*255#設定B通道，R、G通道皆為0
    cv.imshow('create_image',img)



print('---------Hello Python -----------')
src = cv.imread('E:/PyAI/Image/harry.jpg',)
cv.namedWindow('Input Image',cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image",src)
create_image()
# t1 = cv.getTickCount()
# access_pixels(src)
# t2 = cv.getTickCount()
# time = (t2-t1)/cv.getTickFrequency()
# print("Time : %s"%(time*1000))#乘以1000是為讓時間變成毫秒
inverse(src)
cv.waitKey(0) #按0圖片檔會關掉
cv.destroyAllWindows()