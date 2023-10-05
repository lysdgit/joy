import cv2
import numpy as np

# 读取图像
img = cv2.imread('C:/Users/liys2/Desktop/Numocr/0.jpg', cv2.IMREAD_GRAYSCALE)

# 应用拉普拉斯滤波器
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# 将结果转换为8位灰度图像
laplacian = np.uint8(np.absolute(laplacian))

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Laplacian Edge Detection', laplacian)
cv2.imwrite('C:/Users/liys2/Desktop/Numocr/122.jpg', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
