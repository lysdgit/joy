import serial
import time

# 创建串口对象
ser = serial.Serial('COM4', 115200, timeout=1)  # 根据实际情况修改串口号和波特率

# 十六进制字符串
hex_string = 'FEF0030100000000'

while True:
    try:
        # 将十六进制字符串转换为字节对象
        data = bytes.fromhex(hex_string)

        # 发送数据到串口
        ser.write(data)

        # 读取串口数据
        response = ser.read(10)  # 根据实际情况指定读取的字节数
            
        if response:
            # 将返回值转换为十六进制字符串，并打印出来
            hex_response = ' '.join(['{:02X}'.format(byte) for byte in response])
            print('Response:', hex_response)

        # 延时 100 毫秒
        time.sleep(1)

    except serial.SerialException as e:
        print('Serial Port Error:', str(e))

    finally:
    # 关闭串口
        ser.close()
