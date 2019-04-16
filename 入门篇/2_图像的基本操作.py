import cv2
'''
访问和修改图片像素点的值
获取图片的宽、高、通道数等属性
了解感兴趣区域ROI
分离和合并图像通道
'''

img = cv2.imread("0003.png")  # 注意彩色图返回的是BGR格式，gray或者单通道返回的只有一个值

px = img[30, 40]  # 坐标30，40处像素的信息
print(px)

px_blue = img[30, 40, 1]  # 参数： 前两个表示坐标，第三个0-1-2分别表示三个通道B G R
print(px_blue)  # 只获取蓝色通道的值


'''
图片属性
'''
print(img.shape)
