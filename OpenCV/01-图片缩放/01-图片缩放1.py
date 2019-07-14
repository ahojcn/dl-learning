import cv2

img = cv2.imread('../01image.JPG', 1)
img_info = img.shape
print(img_info)

height = img_info[0]
width = img_info[1]
mode = img_info[2]

# 放大和缩小两种，又等比例缩放和非等比例缩放
# 等比例缩放：原始图像的宽高 * 一个相同的系数
# 非等比例缩放：原始宽高 * 不同的系数
# 下面是等比例缩放
dst_height = int(height * 0.5)
dst_width = int(width * 0.5)

# 在 cv 中提供了 4 中常用的缩放方法
# 最近邻域差值、双线性差值、像素关系重采样、立方差值
# 默认采用 双线性差值
dst_img = cv2.resize(img, (dst_width, dst_height))

cv2.imshow('img', img)
cv2.imshow('dst_img', dst_img)
cv2.waitKey(0)

"""
最近邻域插值法 原理：
src 10*20
dst 5*10
dst <- src
(1, 2) <- (2, 4)

new_x = src_x * (src 行 / 目标 行)
例如： (1, 2) 这个点
new_x = 1 * (10 / 5) = 2
new_y = 2 * (20 / 10) = 4

12.3 取 12
"""

"""
双线性差值法 原理：

"""
