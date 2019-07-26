import cv2
import numpy as np

img = cv2.imread('../WindowsLogo.jpg')
rows, cols = img.shape[:2]  # h = rows    w = cols

M2 = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)

dst = cv2.warpAffine(img, M2, (cols, rows))

cv2.imshow('src', img)
cv2.imshow('dst', dst)


cv2.waitKey(0)
