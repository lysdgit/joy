import serial
import time
import datetime

# 创建串口对象
ser = serial.Serial('COM6', 115200, timeout=0.1)

# 十六进制数据
hex_data = bytes.fromhex('FE F0 02 01 00 00 00 00')
while True:
    try:
    # 发送数据到串口
        ser.write(hex_data)

    # 读取串口返回的数据
        response = ser.read(10)  # 根据实际情况指定读取的字节数

        if response:
            # 将返回值转换为十六进制字符串，并打印出来
            hex_response = ' '.join(['{:02X}'.format(byte) for byte in response])
            # print('完整接收:', hex_response)
            # 拆分数据字符串
            data_list = hex_response.split(" ")
            # print('去空格接收:',data_list)

            # 获取右六位数据
            right_six = data_list[-3:]
            # print(right_six)

            zhengshu = int(right_six[0] , 16)
            zhengshu_str = str(zhengshu)

            xiaoshu = ''.join([str(right_six[1]), str(right_six[2])])
            xiaoshu = int(xiaoshu,16)
            xiaoshu_str = str(xiaoshu)

            now_data = zhengshu_str+"."+xiaoshu_str
            print(float(now_data))
          
           # 获取当前时间作为文件名
            current_time = datetime.datetime.now().strftime('%m%d_%H:%M:%S')
            # # 将返回值保存至文件
            with open(r"C:\Users\liys2\Desktop\pyRD\测试传感器\data\12268.csv", 'a') as f:
                 f.write(current_time+','+now_data + '\n')

        # 延时 
        time.sleep(0.1)

    except serial.SerialException as e:
        print('Serial Port Error:', str(e))
    
# 关闭串口
ser.close()

