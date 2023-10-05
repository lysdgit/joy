import cv2
import numpy as np

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/Numocr/raw2.jpg')
height, width, channels = image.shape

# 高斯滤波
gaussian_blur = cv2.GaussianBlur(image, (3, 3), 1)

#灰度化
gray_image = cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2GRAY)

# 中值滤波
median_blur = cv2.medianBlur(gray_image, 1)

# 设置拉伸的上下限
a = 1
b = 255

# 对比度拉伸
stretched_image = np.uint8((b-a) / (np.max(median_blur)-np.min(median_blur)) * (median_blur-np.min(median_blur)) + a)

#直方图均衡化
equalized_image = cv2.equalizeHist(stretched_image)

# 自适应阈值二值化
thresh = cv2.adaptiveThreshold(equalized_image, 222, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)

# # 增加对比度
# alpha = 20  # 对比度增益因子
# beta = 2    # 亮度调整值
# adjusted_image = cv2.convertScaleAbs(thresh, alpha=alpha, beta=beta)

# 创建一个自定义大小的窗口
cv2.namedWindow("Median Blur", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Median Blur", width, height)

# 显示原始图像和滤波后的图像
cv2.imshow('Median Blur', thresh)
# cv2.imshow('Adjusted Image', adjusted_image)
cv2.imwrite('output_image.jpg', thresh)
cv2.imwrite('C:/Users/liys2/Desktop/Numocr/1222.jpg', thresh)
# cv2.imwrite('C:/Users/liys2/Desktop/Numocr/1222.jpg', adjusted_image)


# 等待用户按下任意按键退出程序
cv2.waitKey(0)
cv2.destroyAllWindows()
