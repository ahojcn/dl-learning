import cv2

img = cv2.imread('./OpenCV/01image.jpg', 1)
cv2.imshow('image', img)

cv2.waitKey(0)