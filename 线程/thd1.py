import threading
import serial
import time
import datetime

# 创建串口对象
ser = serial.Serial('COM1', 115200, timeout=1)

def send_receive_data(hex_data):
    # 创建串口对象
    # ser = serial.Serial('COM20', 115200, timeout=0.1)
    while True:
        try:
            # 发送数据到串口
            ser.write(hex_data)

            # 读取串口返回的数据
            response = ser.read(10)  # 根据实际情况指定读取的字节数

            if response:
                # 将返回值转换为十六进制字符串，并打印出来
                hex_response = ' '.join(['{:02X}'.format(byte) for byte in response])
                data_list = hex_response.split(" ")
                
                # # 获取传感器ID号
                # id = data_list[2]
                # print(id)

                # 获取右六位数据
                right_six = data_list[-3:]

                zhengshu = int(right_six[0], 16)
                zhengshu_str = str(zhengshu)

                xiaoshu = ''.join([str(right_six[1]), str(right_six[2])])
                xiaoshu = int(xiaoshu, 16)
                xiaoshu_str = str(xiaoshu)

                if xiaoshu < 1000:
                    now_data = zhengshu_str + ".0" + xiaoshu_str
                    print(float(now_data))
                else:
                    now_data = zhengshu_str + "." + xiaoshu_str
                    print(float(now_data))

                # 获取当前时间
                current_time = datetime.datetime.now().strftime('%m%d_%H:%M:%S')
                # 将返回值保存至文件
                with open(r"C:\Users\liys2\Desktop\pyRD\测试传感器\data\23103001.csv", 'a') as f:
                    f.write(current_time + ',' + now_data + '\n')

            time.sleep(0.1)

        except serial.SerialException as e:
            print('Serial Port Error:', str(e))

    # 关闭串口
    ser.close()

if __name__ == '__main__':

    # 创建第一个线程发送第一个hex_data
    thread1 = threading.Thread(target=send_receive_data, args=(bytes.fromhex('FE F0 01 01 00 00 00 00'),))
    # 创建第二个线程发送第二个hex_data
    # thread2 = threading.Thread(target=send_receive_data, args=(bytes.fromhex('FE F0 02 01 00 00 00 00'),))
    # 创建第三个线程发送第三个hex_data
    # thread3 = threading.Thread(target=send_receive_data, args=(bytes.fromhex('FE F0 03 01 00 00 00 00'),))

    # 启动线程
    thread1.start()
    # thread2.start()
    # thread3.start()

    # 主线程等待子线程结束
    thread1.join()
    # thread2.join()
    # thread3.join()
    print("All threads finished")
