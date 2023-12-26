import serial

# 设置串口参数
ser = serial.Serial('COM8', 115200, timeout=0.1)  # 将'COM1'替换为你的串口号，9600是波特率，timeout是读取超时时间

try:
    while True:
        # 读取串口数据
        data = ser.readline().decode('utf-8').strip()
        
        # 打印读取的数据
        print(data)

except KeyboardInterrupt:
    # 如果通过键盘中断程序，关闭串口
    ser.close()
