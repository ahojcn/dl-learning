"""
实现步骤：
1. 创建一个足够大的画板
2. 将一幅图像分别从前向后、从后向前绘制
3. 绘制中心分割线
"""

import cv2
import numpy as np

img = cv2.imread('../LinuxLogo.jpg', 1)
cv2.imshow('src img', img)

img_info = img.shape
height = img_info[0]
width = img_info[1]
deep = img_info[2]

new_img_info = (height * 2, width, deep)
new_img = np.zeros(new_img_info, np.uint8)

for i in range(0, height):
    for j in range(0, width):
        new_img[i, j] = img[i, j]

        new_img[height * 2 - i - 1, j] = img[i, j]

# 添加分割线
for i in range(0, width):
    new_img[height, i] = (0, 0, 255)  # bgr

cv2.imshow('new img', new_img)
cv2.waitKey(0)
