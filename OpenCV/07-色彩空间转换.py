import cv2 as cv


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
    cv.imshow('bgr', img)

    color_space_demo(img)

    cv.waitKey(0)
    cv.destroyAllWindows()
