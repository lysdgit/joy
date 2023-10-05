import cv2
import numpy as np

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/num/imging/715.png')

# # 定义要替换的颜色和目标颜色
# source_color = np.array([b,b,b])     # BGR颜色值
# target_color = np.array([255,255,255])  # BGR颜色值
# 定义目标颜色
target_color = np.array([0, 0, 0])  # BGR颜色值

# 循环替换颜色
for b in range(140, 198):
    source_color = np.array([b, b, b])  # BGR颜色值

    # 创建一个掩码，标记源颜色的像素
    mask = cv2.inRange(image, source_color, source_color)

    # 将源颜色替换为目标颜色
    image[mask != 0] = target_color

# 创建一个掩码，标记源颜色的像素
mask = cv2.inRange(image, source_color, source_color)

# 将源颜色替换为目标颜色
image[mask != 0] = target_color

# 显示图像
cv2.imshow('Original Image', image)
cv2.imwrite('C:/Users/liys2/Desktop/Numocr/num/imging/ed715.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
