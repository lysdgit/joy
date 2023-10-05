import serial
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM1', 9600)
x_list = []
y_list = []

# 初始化图表
plt.ion()  # 打开交互模式
fig, ax = plt.subplots()
line, = ax.plot([], [])  # 创建空折线图

while True:
    receive = ser.readline()  # 接收传感器响应
    # receive = ser.read_all() # 读取一行数据（以换行符为结束符）
    y = receive.decode()  # 解码获得字符串
    y = y.rsplit(",", 1)[1]  # 将字符串拆分，提取右侧第一个字符串（例如'+055.1234'，或者01）
    y = round(float(y), 4)  # 将字符串转换为浮点数据，并四舍五入取4位小数 
    y_list.append(y)
    x = len(y_list)   
    x_list.append(x)

    # 绘制折线图
    plt.plot(x_list, y_list, marker='o')  # 使用 'o' 标记显示数据点
    plt.xlabel('X轴')  # 设置 x 轴标签
    plt.ylabel('Y轴')  # 设置 y 轴标签
    plt.title('二维点折线图')  # 设置标题

    # 显示图形
    plt.show()
    print(x)
    print(y)


 


# 关闭串口连接
ser.close()
