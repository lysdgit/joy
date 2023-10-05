import cv2
import numpy as np
from scipy import ndimage

def moire_filter(image):
    # 定义奈奎斯特频率
    nyquist_freq = 0.5

    # 计算输入图像的傅里叶变换
    fft = np.fft.fft2(image)

    # 将频谱图进行中心化
    fft_shifted = np.fft.fftshift(fft)

    # 获取频谱图的尺寸
    rows, cols = fft_shifted.shape

    # 计算中心点坐标
    center_row, center_col = int(rows / 2), int(cols / 2)

    # 定义滤波器半径
    radius = int(nyquist_freq * min(rows, cols) / 2)

    # 创建一个圆形滤波器
    mask = np.zeros((rows, cols), dtype=np.uint8)
    cv2.circle(mask, (center_col, center_row), radius, 1, -1)

    # 应用滤波器
    filtered_fft_shifted = fft_shifted * mask

    # 将频谱图反向中心化
    filtered_fft = np.fft.ifftshift(filtered_fft_shifted)

    # 计算滤波后的图像
    filtered_image = np.abs(np.fft.ifft2(filtered_fft))

    # 将像素值缩放到0-255范围
    filtered_image = cv2.normalize(filtered_image, None, 0, 255, cv2.NORM_MINMAX)

    # 将图像转换为8位无符号整数类型
    filtered_image = filtered_image.astype(np.uint8)

    return filtered_image

# 读取图像
image = cv2.imread('C:\\Users\\liys2\\Desktop\\Numocr\\0.jpg', 0)

# 对图像进行滤波
filtered_image = moire_filter(image)

# 显示原始图像和滤波后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.imwrite('C:/Users/liys2/Desktop/Numocr/122.jpg', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

