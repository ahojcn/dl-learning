import cv2
import numpy as np

src = cv2.imread('../sudoku.png')
h, w, d = src.shape

# 原图像上的 4 个点
pts1 = np.float32([
    [56, 65], [368, 52], [28, 387], [389, 390]
])
# 原图像上的点在目标图像上的点映射
pts2 = np.float32([
    [0, 0], [300, 0], [0, 300], [300, 300]
])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(src, M, (300, 300))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
