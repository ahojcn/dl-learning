import cv2

src_img = cv2.imread('../messi5.jpg')

dst_img = src_img[200:700, 300:600]

cv2.imshow('dst', dst_img)
cv2.waitKey(0)
