import cv2

# 读取彩色图像
image = cv2.imread(r"C:\Users\liys2\Desktop\12.png")

# 将彩色图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 显示灰度图像
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 二值化处理
_, binary_image = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY)

# 显示原始图像和二值化图像
# cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # 边缘检测
# edges = cv2.Canny(gray_image, 100, 200)

# # 显示边缘图像
# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

