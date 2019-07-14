import cv2

img = cv2.imread('../01image.JPG', 1)
imgInfo = img.shape

dst = img[200:700, 300:600]

cv2.imshow('image', dst)
cv2.waitKey(0)