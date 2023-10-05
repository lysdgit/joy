import serial
import time

# 创建串口对象
ser = serial.Serial('COM3', 9600, timeout=1)  # 根据实际情况修改串口号和波特率

# 十六进制字符串
hex_string = 'FEF0010100000000'

try:
    while True:
        # 将十六进制字符串转换为字节对象
        data = bytes.fromhex(hex_string)
        
        # 发送数据到串口
        ser.write(data)
        
        # 延时 100 毫秒
        time.sleep(0.1)

        receive = ser.readline()  # 接收传感器响应
        data = receive.decode()  # 解码获得字符串
        # 拆分数据字符串
        data_list = data.split(" ")
        # 获取右六位数据
        right_six = data_list[-3:]
        # print(right_six)

        zhengshu = int(right_six[0] , 16)
        zhengshu_str = str(zhengshu)

        xiaoshu = ''.join([str(right_six[1]), str(right_six[2])])
        xiaoshu = int(xiaoshu,16)
        xiaoshu_str = str(xiaoshu)

        print(zhengshu_str+"."+xiaoshu_str)
        time.sleep(0.1)

    
except serial.SerialException as e:
    print('Serial Port Error:', str(e))

finally:
    # 关闭串口
    ser.close()

