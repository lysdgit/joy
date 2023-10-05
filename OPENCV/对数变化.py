import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/num/imging/rvedatasou1.png', 0)

# 灰度对数变化
c = 255 / np.log(1 + np.max(image))
log_transformed = c * (np.log(image + 1))

# 将图像转换为整数类型
log_transformed = np.array(log_transformed, dtype=np.uint8)

# 显示原始图像和灰度对数变化后的图像
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(log_transformed, cmap='gray'), plt.title('Log Transformed Image')
plt.show()
