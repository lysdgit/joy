import cv2
import numpy as np
import csv

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/num/imging/1.png')

# 将图像转换为BGR颜色空间
bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# 统计像素点的BGR颜色
colors, counts = np.unique(bgr_image.reshape(-1, 3), axis=0, return_counts=True)

# 创建CSV文件并写入标题行
with open('C:/Users/liys2/Desktop/Numocr/num/imging/8.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['B', 'G', 'R', 'Count'])

    # 遍历每个颜色和计数，并将其写入CSV文件
    for color, count in zip(colors, counts):
        writer.writerow([color[0], color[1], color[2], count])

print("CSV文件保存成功！")

# import cv2
# import numpy as np

# # 读取图像
# image = cv2.imread('C:/Users/liys2/Desktop/er.png')

# # 将图像转换为BGR颜色空间
# bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# # 统计像素点的BGR颜色
# colors, counts = np.unique(bgr_image.reshape(-1, 3), axis=0, return_counts=True)

# # 打印结果
# for color, count in zip(colors, counts):
#     print(f'BGR: {color}, Count: {count}')