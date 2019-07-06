import cv2 as cv
import numpy as np


def access_pixels(img):
    """访问每一个像素"""
    print(img.shape)
    height = img.shape[0]  # 宽
    width = img.shape[1]  # 高
    channels = img.shape[2]  # 颜色通道 blue green red (bgr)
    print("width:%s, height:%s, channels:%s" % (width, height, channels))

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                pv = img[i, j, k]
                img[i, j, k] = 255 - pv

    cv.imshow('demo', img)


def create_img():
    # img = np.zeros([400, 400, 3], np.uint8)
    # img[:, :, 0] = np.ones([400, 400]) * 255  # 上色，给 b 通道赋值，400 * 400个像素均为 255（蓝色）
    # img[:, :, 1] = np.ones([400, 400]) * 255  # 与上同理
    # cv.imshow('new image', img)

    # 单通道图片（单通道一般为灰度图片）
    img = np.zeros([400, 400, 1], np.uint8)  # zeros 初始化了一个三维数组，并且里面都是 0
    img[:, :, 0] = np.ones([400, 400]) * 127  # ones 给对应的坐标赋值为 1，如果 * 了 127 就是赋值127呗。
    cv.imshow('new image', img)


if __name__ == '__main__':
    img = cv.imread('01image.JPG', 1)
    # cv.imshow('06', img)

    # t_start = cv.getTickCount()
    # access_pixels(img)
    # t_end = cv.getTickCount()
    # print("time: %s ms" % ((t_end - t_start) / cv.getTickFrequency() * 1000))

    create_img()

    cv.waitKey(0)
    cv.destroyAllWindows()
