import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread("C:/Users/liys2/Desktop/Numocr/num/imging/rvemdatasou1.png", 0)  # 以灰度模式读取图像

# # 进行高斯滤波
# filtered_image = cv2.GaussianBlur(image, (5, 5), 0)

# # 显示原始图像和滤波后的图像
# cv2.imshow('Original Image', image)
# cv2.imshow('Filtered Image', filtered_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 应用中值滤波
filtered_image = cv2.medianBlur(image, 3)  # 使用3x3的滤波器

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 应用均值滤波
filtered_image = cv2.blur(image, (3, 3))  # 使用3x3的滤波器

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 进行直方图均衡化
equalized_image = cv2.equalizeHist(image)

# 显示原始图像和均衡化后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 计算直方图
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# 绘制直方图
plt.plot(hist)
plt.xlabel("灰度级别")
plt.ylabel("像素数量")
plt.show()
