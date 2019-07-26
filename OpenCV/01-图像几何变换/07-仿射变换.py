import cv2
import numpy as np

src = cv2.imread('../WindowsLogo.jpg')
r, c, d = src.shape
print(r, c, d)

# 原图像上的三个点
pts1 = np.float32([
    [0, 0],  # 左上角
    [0, r - 1],  # 左下角
    [c - 1, 0]  # 右上角
])
# 新图像上的三个点
pts2 = np.float32([
    [50, 50],
    [30, r - 20],
    [c - 30, 10]
])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(src, M, (c, r))

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey(0)
