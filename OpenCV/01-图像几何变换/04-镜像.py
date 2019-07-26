import cv2
import numpy as np

img = cv2.imread('../LinuxLogo.jpg')

h, w, d = img.shape[:3]

new_img_info = (h * 2, w, d)
new_img = np.zeros(new_img_info, np.uint8)

for i in range(0, h):
    for j in range(0, w):
        new_img[i, j] = img[i, j]
        new_img[h * 2 - i - 1, j] = img[i, j]

cv2.imshow('new_img', new_img)
cv2.waitKey(0)