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
print(img.shape)  # 同样的彩色图输出 图片大小 通道数量，gray图片返回大小

print(img.dtype)  # 经验之谈：很多错误都是因为数据类型不对导致的，所以健壮的代码应该对这个属性加以判断。

print(img.size)   # 获取图片的像素= 长*宽*通道数量

'''
截取图片ROI,可以按照距离进行划分
'''
num1 = img[0:46, 0:30]
num2 = img[0:46, 31:60]
num3 = img[0:46, 61:90]
num4 = img[0:46, 91:120]
cv2.imshow('nums1', num1)
cv2.imshow('nums2', num2)
cv2.imshow('nums3', num3)
cv2.imshow('nums4', num4)
cv2.waitKey(0)

b, g, r = cv2.split(img)
# 这样可以得到三个通道的颜色，同样也可以使用numpy的索引，例如 b = img[:, :, 0]
