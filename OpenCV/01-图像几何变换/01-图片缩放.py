import cv2
import numpy as np

img = cv2.imread('../messi5.jpg')
cv2.imshow('img', img)

bg_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('bg_img', bg_img)

height, width = img.shape[:2]
sm_img = cv2.resize(img, (int(0.5*width), int(0.5*height)), interpolation=cv2.INTER_AREA)
cv2.imshow('sm_img', sm_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
