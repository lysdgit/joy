import numpy as np
import cv2
from scipy import fftpack

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/num/imging/rvedatasou1.png', cv2.IMREAD_GRAYSCALE)

# 进行傅里叶变换
image_fft = fftpack.fftshift(fftpack.fft2(image))

# 定义滤波器
mask = np.zeros_like(image_fft)
mask[200:400, 200:400] = 1

# 进行频域滤波
filtered_image = fftpack.ifft2(fftpack.ifftshift(image_fft * mask)).real
filtered_image = np.uint8(filtered_image)

# 显示结果
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()