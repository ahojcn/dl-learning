import cv2
import numpy as np

img = cv2.imread('../messi5.jpg', 1)
cv2.imshow('src', img)

img_info = img.shape
height = img_info[0]
width = img_info[1]

mat_shift = np.float32([
    [1, 0, 100], [0, 1, 200]
])  # 2 * 3 的移位矩阵

# 原始图片，移位矩阵，宽高
dst = cv2.warpAffine(img, mat_shift, (height, width))

cv2.imshow('dst', dst)
cv2.waitKey(0)

"""
移位 api 原理
[[1, 0, 100], [0, 1, 200]]   2 * 3
[[1, 0], [0, 1]]  2*2  A
[[100], [200]]  2*1  B
C x, y
A * C + B = [[1 * x + 0 * y], [0 * x + 1 * y]] + [[100], [200]]
     = [[x+100], [y+200]]
所以这个移位矩阵就相当于 向右移动100点，向下移动200点
"""
