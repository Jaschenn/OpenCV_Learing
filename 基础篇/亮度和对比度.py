import cv2
import numpy as np
import matplotlib.pylab as plt
img = cv2.imread("937_a_0.png")
res = np.uint8(np.clip((1.5 * img + 10), 0, 255))
# g(x) = a*f(x) + c a对比度，c为亮度
'''
参数说明：
np.clip(用来限制参数的大小，第一个参数就是需要进行变换的参数，第二个第三个分别为最小值，最大值)
'''
tmp = np.hstack((img, res))  # 两张图进行合并，方便对比
plt.imshow(tmp)
plt.show()