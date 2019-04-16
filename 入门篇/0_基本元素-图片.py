import cv2

img = cv2.imread("0003.png",0)
'''
第二个参数表示读取方式：
cv2.IMREAD_COLOR：彩色图，默认值(1)
cv2.IMREAD_GRAYSCALE：灰度图(0)
cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)

'''
cv2.imshow("img",img)
# 第一个参数表示窗口名称，第二个表示图像。若需要显示多个，只需要设置同样的窗口名称就可以
cv2.waitKey(0)
# 表示的是需要等待的时间，0表示一直等待。程序会在这里暂停。

cv2.imwrite("./grag_0003.png",img)
# 参数表示的是名称，第二个表示图片。
