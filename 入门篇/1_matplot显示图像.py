import cv2
import matplotlib.pyplot as plt

img = cv2.imread("0003.png", 0)

img2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# cv2使用BGR方式打开图片，但是plt使用RGB方式，这里需要翻转一下俩个通道。否则颜色会不正常
plt.subplot(1, 2, 1)
# 一行，两列第一个位置
plt.imshow(img)
plt.subplot(1, 2, 2)
# 一行 两列，第二个位置
plt.imshow(img2)
plt.show()


