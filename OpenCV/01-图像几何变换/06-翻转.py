import cv2

src = cv2.imread('../LinuxLogo.jpg')

dst1 = cv2.flip(src, 1)
dst0 = cv2.flip(src, 0)
dst_1 = cv2.flip(src, -1)

cv2.imshow('src', src)
cv2.imshow('dst0', dst0)
cv2.imshow('dst1', dst1)
cv2.imshow('dst_1', dst_1)

cv2.waitKey(0)