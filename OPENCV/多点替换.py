import cv2
import numpy as np

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/num/imging/ed7144.png')

# 将图像转换为BGR颜色空间
bgr_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 统计每个像素点的BGR颜色和计数
color_counts = np.unique(bgr_image.reshape(-1, 3), axis=0, return_counts=True)

n=1700

# 将出现次数超过n的点源颜色替换为目标颜色
for color, count in zip(color_counts[0], color_counts[1]):
    if count > n:
        bgr_image[np.all(bgr_image == color, axis=-1)] = [255, 255, 255]  # 目标颜色为黑色

# 将图像转换回RGB颜色空间
result_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

# 保存结果图像
cv2.imshow('Image', result_image)
cv2.waitKey(0)
cv2.imwrite('C:/Users/liys2/Desktop/Numocr/num/imging/edatasou2.png', result_image)
