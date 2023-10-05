import os
import re
import sys

from RapidOCR_api import OcrAPI

ocrPath = 'D:\Program Files\RapidOCR-json\\RapidOCR_json.exe'  # OCR识别依赖程序
ocr = OcrAPI(ocrPath)
res = ocr.run('C:/Users/liys2/PycharmProjects/pythonProject/recive_img1.jpg')  # OCR识别的图片来源路径
code_value = res['code']
# print(code_value)
print('OCR识别结果：\n', res)

if code_value == 100:
    # img.txt为识别后保存的路径
    with open(r"C:\Users\liys2\PycharmProjects\pythonProject\img.txt", "w", encoding="utf-8") as file:
        for region in res['data']:
            detected_text = region['text']
            detected_text = re.sub(r'[a-zA-Z]', '', detected_text)
            detected_text = re.sub(r'@', '', detected_text)
            detected_text = re.sub(r':', '.', detected_text)
            detected_text = detected_text[:7]
            # print(detected_text)
            file.write(detected_text + ',')
    print("内容已保存到img.txt文件中。")
    ocr.stop()

if code_value == 101:
    with open(r"C:\Users\liys2\PycharmProjects\pythonProject\img.txt", "w", encoding="utf-8") as file:
        file.write("888.888,888.888,888.888,888.888,888.888,888.888")
    print("内容已保存到img.txt文件中。")
