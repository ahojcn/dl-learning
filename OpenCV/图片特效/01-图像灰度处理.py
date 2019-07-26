import cv2

""" 1 """
# img0 = cv2.imread('../messi5.jpg', 0)
# img1 = cv2.imread('../messi5.jpg', 1)
# print(img0.shape)
# print(img1.shape)
# cv2.imshow('src', img0)
# cv2.waitKey(0)

""" 2 """
img1 = cv2.imread('../messi5.jpg', 1)
dst = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 颜色控件转换
cv2.imshow('dst', dst)
cv2.waitKey(0)
