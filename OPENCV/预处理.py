import cv2
import numpy as np

# 读取图片
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/212.jpg', cv2.IMREAD_GRAYSCALE)

# 图片去噪
denoised_image = cv2.fastNlMeansDenoising(image, None, 1, 100, 1)

# 图片二值化
_, binary_image = cv2.threshold(denoised_image, 0, 100, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 反色
inverted_image = cv2.bitwise_not(binary_image)

# 将黑底变为白底，字变为黑色
output_image = np.where(inverted_image == 255, 2, 255).astype(np.uint8)

# 保存处理后的图片
cv2.imwrite('output_image.jpg', output_image)
