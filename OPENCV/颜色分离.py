
import cv2 as cv
import numpy as np
 
img = cv.imread(r'C:/Users/liys2/Desktop/Numocr/12.jpg')
img = cv.resize(img, (357, 625))
# BGR通道分离
B, G, R = cv.split(img)
# BGR转RGB(合并通道)
img_rgb1 = cv.merge([R, G, B])
cv.imshow("BGR", img_rgb1)
cv.waitKey(0)
# 再次BGR通道分离
B, G, R = cv.split(img_rgb1)
cv.imshow("B chanel", B)


# 图像预处理
# 滤波器模糊处理
blur = cv.blur(img_rgb1, (5, 5))
blur0 = cv.medianBlur(blur, 3)
blur1 = cv.GaussianBlur(blur0, (3, 3), 0)
blur2 = cv.bilateralFilter(blur1, 5, 75, 75)
# cv.imshow("after blur", blur0)


# HSV空间中，三者相对独立，可以准确描述像素的亮度，饱和度和色度
hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
# 颜色分割：阈值分割，需要尝试
low_blue = np.array([80, 50, 50])
high_blue = np.array([150, 255, 255])
# “Mask”将所有不在描述对象范围内的其他像素进行覆盖
mask = cv.inRange(hsv, low_blue, high_blue)
res = cv.bitwise_and(img_rgb1, img_rgb1, mask=mask)
# cv.imshow("mask...", res)
# cv.waitKey(0)
 
# 取灰度图
gary = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
cv.imshow("gary", gary)
cv.waitKey(0)
 
 
# 二值化，取阈值为30
ret, binary_img = cv.threshold(gary, 30, 255, 0)
cv.imshow("binary_img", binary_img)
cv.waitKey(0)
 
# 膨胀0
dilate = cv.dilate(binary_img, None, iterations=4)
cv.imshow("dilate0 image", dilate)
cv.waitKey(0)
# 开运算
kernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))
open = cv.morphologyEx(dilate, cv.MORPH_OPEN, kernel)
cv.imshow("open image", open)
cv.waitKey(0)
# 闭运算
closing = cv.morphologyEx(open, cv.MORPH_CLOSE, (9, 9))
cv.imshow("closing image", closing)
cv.waitKey(0)
 
# # 膨胀
dilate = cv.dilate(closing, None, iterations=3)
cv.imshow("dilate1 image", dilate)
cv.waitKey(0)
# 腐蚀
erode = cv.erode(closing, None, iterations=3)
cv.imshow("erode1 image", erode)
cv.waitKey(0)
# 闭运算
closing = cv.morphologyEx(erode, cv.MORPH_CLOSE, (5, 5))
cv.imshow("closing image2", closing)
cv.waitKey(0)
 
 
 
# 寻找图像中的轮廓
contours, hierarchy = cv.findContours(closing, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# 绘制独立轮廓(边缘拟合)
img = cv.drawContours(img, contours, -1, (0, 0, 255), 2)
 
 
for i in range(3):
    # 21.2 轮廓特征
    cnt = contours[i]
    # 21.2.2轮廓面积
    area = cv.contourArea(cnt)
    # 21.2.3轮廓周长
    perimeter = cv.arcLength(cnt, True)
 
    # 21.2.7 边界矩形
    # 有两类边界矩形
    """
    1、直边界矩形: 一个直矩形（就是没有旋转的矩形）,它不会考虑对象是否旋转,所以边界矩形的面积不是最小的。
                 可以使用函数 cv2.boundingRect() 查找得到。
    （x，y）为矩形左上角的坐标，（w，h）是矩形的宽和高。
    """
    # x, y, w, h = cv.boundingRect(cnt)
    # # 绘制矩形：使用对角线的两点(x, y), (x + w, y + h)画一个矩形轮廓
    # img = cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    """
    2、旋转的边界矩形：这个边界矩形是面积最小的，因为它考虑了对象的旋转。用到的函数为 cv2.minAreaRect()。
    """
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    im = cv.drawContours(img, [box], 0, (0, 255, 0), 2)
 
cv.imshow("contour", img)
cv.waitKey(0)
