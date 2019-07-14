import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([3, 5, 7, 0, 12, 2, 1, 15])

# 绘制折线图
# x，y，颜色，lw=线宽
plt.plot(x, y, 'r')
plt.plot(x, y, 'g', lw=10)
# plt.show()

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([3, 5, 7, 0, 12, 2, 1, 15])

# 绘制柱状图
# x,y,柱状图宽度百分比，alpha=透明度，color=颜色
plt.bar(x, y, 0.5, alpha=1, color='b')
plt.show()
