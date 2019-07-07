import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)  # 从 0 号摄像头读取，可能电脑上有多个摄像头，从0开始编号
    while True:
        recv, frame = capture.read()
        frame = cv.flip(frame, 1)  # 摄像头翻转
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_img_info(img):
    print(type(img))
    print(img.shape)
    print(img.size)
    print(img.dtype)

    pixel_data = np.array(img)  # 获取像素数据
    print(pixel_data)  # 打印像素数据


if __name__ == '__main__':
    img = cv.imread('01image.JPG', 1)  # 加载图片

    # cv.imshow('01image', img)  # 展示图片
    # get_img_info(img)  # 获取图片信息

    # gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # bgr 转 灰度图
    # cv.imwrite('./05-imageResult.png', gray_img)  # 把这个灰度图写到文件
    video_demo()

    cv.waitKey(0)
    cv.destroyAllWindows()
