import cv2
import numpy as np

img = cv2.imread('../messi5.jpg', 1)
cv2.imshow('src', img)

img_info = img.shape
height = img_info[0]
width = img_info[1]

# 3 点确定一个平面
# 仿射变换就是将 原图像 上的三个点映射到 目标图片 新的位置上
mat_src = np.float32([[0, 0], [0, height - 1], [width - 1, 0]])
mat_dst = np.float32([[50, 50], [30, height - 20], [width - 30, 10]])

# 参数：原图像三个点的位置，这三个点的新的位置
mat_affine = cv2.getAffineTransform(mat_src, mat_dst)
dst = cv2.warpAffine(img, mat_affine, (width, height))

cv2.imshow('dst', dst)
cv2.waitKey(0)
