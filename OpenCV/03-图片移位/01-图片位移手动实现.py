import cv2
import numpy as np

img = cv2.imread('../messi5.jpg', 1)
cv2.imshow('src', img)

img_info = img.shape
height = img_info[0]
width = img_info[1]

dst = np.zeros(img.shape, np.uint8)

for i in range(0, height):
    for j in range(0, width - 100):
        dst[i, j+100] = img[i, j]

cv2.imshow('dst', dst)
cv2.waitKey(0)
