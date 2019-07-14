import cv2 as cv
import numpy as np


def fill_color_demo(img):
    copy_img = img.copy()
    h, w = img.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copy_img, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_color_demo', copy_img)

    # 二值图像填充


def main():
    img = cv.imread('messi5.jpg')
    cv.namedWindow('messi', cv.WINDOW_AUTOSIZE)
    cv.imshow('messi', img)

    # ROI(Region of Interest) 操作
    # face = img[65:185, 146:268]
    # face_gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
    # back_face = cv.cvtColor(face_gray, cv.COLOR_GRAY2BGR)
    # img[65:185, 146:268] = back_face
    # cv.imshow('face', img)
    fill_color_demo(img)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
