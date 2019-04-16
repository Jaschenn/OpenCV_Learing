'''
目标：
模糊。平滑图片来消除图片噪声
函数
blur()
GaussianBlur()
medianBlur()
bilateralFilter()
'''
import cv2
import numpy
import matplotlib.pylab as plt
'''
关于卷积和滤波：
它们都属于卷积，不同滤波方法之间只是卷积核不同（对线性滤波而言）
低通滤波器是模糊，高通滤波器是锐化
低通滤波器就是允许低频信号通过，在图像中边缘和噪点都相当于高频部分，所以低通滤波器用于去除噪点、平滑和模糊图像。
高通滤波器则反之，用来增强图像边缘，进行锐化处理。
'''
'''
噪声：
常见噪声有椒盐噪声和高斯噪声，椒盐噪声可以理解为斑点，随机出现在图像中的黑点或白点；
高斯噪声可以理解为拍摄图片时由于光照等原因造成的噪声。
'''

img = cv2.imread("937_a_0.png")
plt.imshow(img)
plt.show()
blur = cv2.blur(img, (3, 3))  # 均值滤波
plt.imshow(blur)
plt.show()
blur = cv2.boxFilter(img, -1, (3, 3))  # 方框滤波
plt.imshow(blur)
plt.show()
blur = cv2.GaussianBlur(img, (3, 3), 1)  # 高斯滤波,可以有效消除高斯噪音，保留更多的图像细节
plt.imshow(blur)
plt.show()
blur = cv2.medianBlur(img, 5)  # 中值滤波，孤立的斑点容易去除掉，0和255很容易去掉，用于消除椒盐和斑点
plt.imshow(blur)
plt.show()
'''
以上操作都会让图像变模糊，尤其是线性的滤波器。
'''
blur = cv2.bilateralFilter(img, 9, 75, 75)  # 双边滤波
plt.imshow(blur)
plt.show()
"""
在不知道用什么滤波器好的时候，优先高斯滤波cv2.GaussianBlur()，然后均值滤波cv2.blur()。
斑点和椒盐噪声优先使用中值滤波cv2.medianBlur()。
要去除噪点的同时尽可能保留更多的边缘信息，使用双边滤波cv2.bilateralFilter()。
线性滤波方式：均值滤波、方框滤波、高斯滤波（速度相对快）。
非线性滤波方式：中值滤波、双边滤波（速度相对慢）。

"""