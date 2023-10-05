import serial

ser = serial.Serial('COM4', 115200)

while True:
    ser.write(b'FE F0 03 01 00 00 00 00')  # 发送指令
    # ser.write(b'\xFE\xF0\x01\x01\x00\x00\x00\x00')
    # hex_string = 'FEF0030100000000'

    # # 将十六进制字符串转换为字节对象
    # data = bytes.fromhex(hex_string)

    # # 发送数据到串口
    # ser.write(data)

    receive = ser.readline()  # 接收传感器响应
    data = receive.decode()  # 解码获得字符串

    # 拆分数据字符串
    data_list = data.split(" ")
    # print(data_list)

    # 获取右六位数据
    right_six = data_list[-3:]
    # print(right_six)

    zhengshu = int(right_six[0] , 16)
    zhengshu_str = str(zhengshu)

    xiaoshu = ''.join([str(right_six[1]), str(right_six[2])])
    xiaoshu = int(xiaoshu,16)
    xiaoshu_str = str(xiaoshu)

    print(zhengshu_str+"."+xiaoshu_str)
    # # 提取并保存数据
    # a = int(right_six[0], 16)
    # b = int(right_six[1], 16)
    # c = int(right_six[2], 16)

    # print(f"a: {a}")
    # print(f"b: {b}")
    # print(type(c))
    # print(f"c: {c}")

# 关闭串口连接
ser.close()