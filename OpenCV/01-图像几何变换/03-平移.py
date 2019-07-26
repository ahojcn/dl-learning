import cv2
import numpy as np

img = cv2.imread('../messi5.jpg')

M = np.float32([[1, 0, 100], [0, 1, 50]])

height, width = img.shape[:2]

moved_img = cv2.warpAffine(img, M, (width, height))

cv2.imshow('moved_img', moved_img)
cv2.waitKey(0)
