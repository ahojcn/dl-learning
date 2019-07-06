import cv2 as cv
import numpy as np


def extrace_obj_demo():
    capture = cv.VideoCapture("/Users/hanoi_ahoj/Downloads/2.mp4")
    while True:
        ret, frame = capture.read()
        # 当视频流读完的时候，ret 就为 False
        if not ret:
            break

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([35, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow('video', frame)
        cv.imshow('mask', mask)

        c = cv.waitKey(40)
        if c == 27:
            break


# 色彩空间转换
def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)

    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('yuv', yuv)

    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('ycrcb', ycrcb)


if __name__ == '__main__':
    img = cv.imread('01image.JPG', 1)

    # cv.imshow('bgr', img)
    # color_space_demo(img)

    # extrace_obj_demo()

    # 通道分离和合并
    cv.imshow('bgr', img)
    b, g, r = cv.split(img)
    cv.imshow('blue', b)
    cv.imshow('green', g)
    cv.imshow('red', r)

    img[:, :, 2] = 0  # red
    cv.imshow('change image', img)

    img = cv.merge([b, g, r])
    cv.imshow('merge', img)

    cv.waitKey(0)
    cv.destroyAllWindows()
