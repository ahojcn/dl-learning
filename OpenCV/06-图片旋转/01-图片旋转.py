import cv2

img = cv2.imread('../WindowsLogo.jpg', 1)
cv2.imshow('src', img)

imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

# 旋转矩阵
# getRotationMatrix2D 得到一个旋转矩阵
# 参数：旋转中心点、旋转角度、缩放系数
matRotate = cv2.getRotationMatrix2D((height*0.5, width*0.5), 45, 1)

dst = cv2.warpAffine(img, matRotate, (height, width))

cv2.imshow('dst', dst)
cv2.waitKey(0)
