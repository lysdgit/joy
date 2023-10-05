import cv2
import numpy as np

# 读取原始图像
img = cv2.imread('C:/Users/liys2/Desktop/Numocr/num/imging/datasou1.png')

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 将灰度图像转换为浮点型
gray = gray.astype(np.float32)

# 使用梯度法锐化图像
gradient_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
gradient = cv2.subtract(gradient_x, gradient_y)

# 将梯度图像转换为8位灰度图像
gradient = cv2.convertScaleAbs(gradient)

# 显示结果图像
cv2.imshow('Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
