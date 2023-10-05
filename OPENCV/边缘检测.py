import cv2
import numpy as np

# 读取图片
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/12.jpg', cv2.IMREAD_GRAYSCALE)

# 边缘检测
edges = cv2.Canny(image, 700, 100)

# 转为RGB图像并创建纯色背景
colored_edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
background_color = (200, 187, 200)  # 绿色背景，可根据需要自定义颜色

# 将边缘赋予颜色
colored_edges[edges != 0] = background_color

# 合并边缘图和原图
final_image = cv2.addWeighted(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR), 1, colored_edges, 5, 0)

# 保存处理后的图片
cv2.imwrite('output_image.jpg', final_image)
