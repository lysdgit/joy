import numpy as np
import cv2

def image_smoothing(image, kernel_size):
    # 创建一个平滑滤波器
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
    
    # 应用滤波器
    smoothed_image = cv2.filter2D(image, -1, kernel)
    
    return smoothed_image

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/212.jpg')

# 调用平滑滤波函数
smoothed_image = image_smoothing(image, 5)

# 显示原图和平滑后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
