import cv2
import matplotlib.pylab as plt
import numpy as np
'''
目标：
旋转，平移，缩放图片
函数：
resize() flip() warpAffine()
'''
img = cv2.imread("0003.png")
plt.subplot(3, 1, 1)
plt.imshow(img)
# 按照指定的宽度，高度缩放图片
res = cv2.resize(img, (240, 40))
plt.subplot(3, 1, 2)
plt.imshow(res)
# 按照比例缩放，如x，y均放大一倍
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
plt.subplot(3, 1, 3)
plt.imshow(res2)
plt.show()
'''
翻转图片
'''
dst = cv2.flip(img, 1)
# 参数2 = 0：垂直翻转(沿x轴)，参数2 > 0: 水平翻转(沿y轴)，参数2 < 0: 水平垂直翻转。
plt.imshow(dst)
plt.show()
'''
旋转图片
'''
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((rows / 2, cols / 2), 45, 0.5)
'''
参数1：图片的旋转中心
参数2：旋转角度(正：逆时针，负：顺时针)
参数3：缩放比例，0.5表示缩小一半
'''
dst = cv2.warpAffine(img, M, (cols, rows))
plt.imshow(dst)
plt.show()
