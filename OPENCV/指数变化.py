import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/num/imging/rvedatasou1.png', 0)

# 灰度指数变化
gamma = 0.5  # 指数值，可根据需要进行调整
gamma_transformed = np.power(image, gamma)

# 将图像转换为整数类型
gamma_transformed = np.array(gamma_transformed, dtype=np.uint8)

# 显示原始图像和灰度指数变化后的图像
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(gamma_transformed, cmap='gray'), plt.title('Gamma Transformed Image')
plt.show()
