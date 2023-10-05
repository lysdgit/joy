import cv2
import numpy as np

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/input.jpg', cv2.IMREAD_GRAYSCALE)

# 对图像应用Sobel算子
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # 水平边缘检测
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # 垂直边缘检测

# 将结果转换为无符号8位整数
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

# 将水平和垂直边缘图像合并
sobel = cv2.addWeighted(sobelx, 0.4, sobely, 0.4, 0)

# 显示结果
cv2.imshow('Sobel', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
