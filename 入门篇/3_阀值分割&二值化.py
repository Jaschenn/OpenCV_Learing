import cv2
import matplotlib.pylab as plt
img = cv2.imread("0003.png", 0)
# 阀值分割
ret1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 6)
# ret是return的缩写，代表的是当前的阀值
ret2, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

plt.subplot(1, 2, 1)
plt.imshow(ret1, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(th2, cmap="gray")
plt.show()

'''
使用ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
来进行固定阀值

'''
'''
自适应的参数列表：
参数1：要处理的原图
参数2：最大阈值，一般为255
参数3：小区域阈值的计算方式
ADAPTIVE_THRESH_MEAN_C：小区域内取均值
ADAPTIVE_THRESH_GAUSSIAN_C：小区域内加权求和，权重是个高斯核
参数4：阈值方式（跟前面讲的那5种相同）
参数5：小区域的面积，如11就是11*11的小块
参数6：最终阈值等于小区域计算出的阈值再减去此值
'''