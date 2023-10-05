import bluetooth
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import base64
import re
from RapidOCR_api import OcrAPI

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
bluetooth.advertise_service(server_sock, "SampleServer", service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            # protocols=[bluetooth.OBEX_UUID]
                            )

print("等待连接")

client_sock, client_info = server_sock.accept()
print("连接成功")

while True:
    stringImg = b""
    c = 0
    try:
        start = time.time()
        while True:
            data = client_sock.recv(1024 * 1024 * 64 * 16)
            stringImg = b"".join([stringImg, data])
            if data.endswith(b"stop"):
                break
            c += 1

    except IOError:
        print("Error")
        pass
    stringImg.strip(b"stop")

    img_decode = base64.decodestring(stringImg)
    img_result = open('recive_img.jpg', 'wb')
    img_result.write(img_decode)

    img_result.close()
    print("Time required ", time.time() - start, "No of iterations ", c)
    print("Image successfully received ")
    img = mpimg.imread('recive_img.jpg')
    imgplot = plt.imshow(img)
    plt.axis('off')
    # plt.show()

    ocrPath = 'D:/Program Files/RapidOCR-json/RapidOCR_json.exe'  # OCR识别依赖程序
    ocr = OcrAPI(ocrPath)
    res = ocr.run('C:/Users/liys2/PycharmProjects/pythonProject/recive_img.jpg')  # OCR识别的图片来源路径
    code_value = res['code']

    if code_value == 100:
        # img.txt为识别后保存的路径
        with open(r"C:\Users\liys2\PycharmProjects\pythonProject\img.txt", "w", encoding="utf-8") as file:
            for region in res['data']:
                detected_text = region['text']
                detected_text = re.sub(r'[a-zA-Z]', '', detected_text)
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

print("Disconnected.")
client_sock.close()
server_sock.close()
print("All done.")