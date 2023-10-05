import cv2

def remove_moire(image_path):
    # 读取图像
    image = cv2.imread("C:/Users/liys2/Desktop/Numocr/1009.jpg")

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用高斯滤波去除噪声
    blurred = cv2.GaussianBlur(gray, (3, 3), 1)

    # 使用自适应阈值二值化图像
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 使用形态学操作去除小的噪点
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # 执行图像减法操作
    result = cv2.subtract(blurred, opening)

    # 显示结果图像
    # cv2.imshow("Gray Image", gray)
    # cv2.imshow("gass Image", blurred)
    cv2.imshow("Moire Removed Image", result)
    cv2.imwrite('C:/Users/liys2/Desktop/Numocr/122.jpg', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 调用函数去除摩尔纹
remove_moire("input_image.jpg")
