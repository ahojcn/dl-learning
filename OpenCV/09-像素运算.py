"""
像素运算
    算术运算
        加减乘除，应用：调节亮度、调整对比度
    逻辑运算
        与或非，应用：遮罩层控制
"""
import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow('add_demo', dst)


def sub_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow('sub_demo', dst)


def div_demo(m1, m2):
    dst = cv.divide(m2, m1)
    cv.imshow('div_demo', dst)


def mul_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow('mul_demo', dst)


def other_demo(m1, m2):
    # im1 = cv.mean(m1)  # 求平均值，均值可以说明这个图像的主色调是什么
    # im2 = cv.mean(m2)

    im1, dev1 = cv.meanStdDev(m1)  # 得到均值和方差
    im2, dev2 = cv.meanStdDev(m2)  # 方差表示图片之间的差异性（对比度），方差是一个小于某个值，可能图像是无效的
    print('img1', im1, dev1)
    print('img2', im2, dev2)


def logic_demo(m1, m2):
    dst = cv.bitwise_and(m1, m2)  # 与运算，做遮罩
    cv.imshow('and', dst)
    dst = cv.bitwise_or(m1, m2)  # 或运算
    cv.imshow('or', dst)
    dst = cv.bitwise_not(m2)  # 非操作，就是 255 - px
    cv.imshow('not', dst)
    dst = cv.bitwise_xor(m1, m2)  # 亦或运算
    cv.imshow('xor', dst)


def contrast_brightness_demo(image, c, b):
    """c 对比度；b 亮度"""
    h, w, ch = image.shape  # 获取shape的数值，height和width、通道

    # 新建全零图片数组src2,将height和width，类型设置为原图片的通道类型(色素全为零，输出为全黑图片)
    blank = np.zeros([h, w, ch], image.dtype)

    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow('contrast_brightness_demo', dst)


if __name__ == '__main__':
    img1 = cv.imread('LinuxLogo.jpg')
    img2 = cv.imread('WindowsLogo.jpg')
    # print('img1' + str(img1.shape))
    # print('img2' + str(img2.shape))
    #
    # cv.namedWindow('img1', cv.WINDOW_AUTOSIZE)
    # cv.imshow('img1', img1)
    # cv.imshow('img2', img2)
    #
    # add_demo(img1, img2)
    # sub_demo(img1, img2)
    # div_demo(img1, img2)
    # mul_demo(img1, img2)
    #
    # other_demo(img1, img2)
    #
    # logic_demo(img1, img2)

    test = cv.imread('01image.JPG')
    contrast_brightness_demo(test, 1.5, 50)

    cv.waitKey(0)
    cv.destroyAllWindows()
