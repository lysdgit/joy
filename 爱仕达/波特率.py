import serial.tools.list_ports

target_baudrate = 9600  # 目标波特率

# 获取所有可用的串口信息
ports = serial.tools.list_ports.comports()

# 遍历所有串口
for port in ports:
    print(port.device)  # 打印串口名称

    # 如果找到目标串口，创建串口对象
    if '目标串口名称' in port.device:
        ser = serial.Serial(port.device, baudrate=target_baudrate)  # 创建串口对象
        break

# 确保已成功创建串口对象
if ser.is_open:
    print('已成功创建串口对象')
else:
    print('未找到目标串口')
