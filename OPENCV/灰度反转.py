import cv2
import numpy as np

# 读取图像
img = cv2.imread('C:/Users/liys2/Desktop/Numocr/122.jpg', 0)

# 灰度反转
reversed_img = 255 - img

# 显示图像
cv2.imshow('Reversed Grayscale Image', reversed_img)
cv2.imwrite('C:/Users/liys2/Desktop/Numocr/num/imging/7141.png',reversed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
