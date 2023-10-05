import cv2
import numpy as np

def correct_perspective(image, pts):
    # 定义目标图像的四个角点
    target_pts = np.float32([[0, 0], [800, 0], [800, 600], [0, 600]])

    # 计算透视变换矩阵
    M = cv2.getPerspectiveTransform(pts, target_pts)

    # 进行透视变换
    result = cv2.warpPerspective(image, M, (800, 600))

    return result

# 读取图像
image = cv2.imread('C:/Users/liys2/Desktop/datasou.png')

# 定义原始图像的四个角点
pts = np.float32([[141, 131], [480, 159], [493, 630], [64, 601]])

# 进行视图矫正
result = correct_perspective(image, pts)

# 显示结果
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
