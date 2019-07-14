import cv2
import numpy as np

src_img = cv2.imread('../WindowsLogo.jpg', 1)

src_img_info = src_img.shape
src_img_height = src_img_info[0]
src_img_width = src_img_info[1]

dst_img_height = int(src_img_height / 2)
dst_img_width = int(src_img_width / 2)
dst_img = np.zeros((dst_img_height, dst_img_width, 3), np.uint8)  # 0-255

for dst_x in range(0, dst_img_height):  # 行
    for dst_y in range(0, dst_img_width):  # 列
        src_x = int(dst_x * (src_img_height * 1.0 / dst_img_height))
        src_y = int(dst_y * (src_img_width * 1.0 / dst_img_width))
        dst_img[dst_x, dst_y] = src_img[src_x, src_y]

cv2.imshow('src_img', src_img)
cv2.imshow('dst_img', dst_img)
cv2.waitKey(0)
