import serial
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM1', 115200)
x = np.arange(1, 62)
# 初始化图表
plt.ion()  # 打开交互模式
fig, ax = plt.subplots()
line, = ax.plot([], [])  # 创建空折线图

# 循环读取数据并更新图表
while True:
    ser.write(b'SR,01,001\r\n')  # 发送指令，
    receive = ser.readline()  # 接收传感器响应
    # receive = ser.read_all() # 读取一行数据（以换行符为结束符）
    y = receive.decode()  # 解码获得字符串
    y = y.rsplit(",", 1)[1]  # 将字符串拆分，提取右侧第一个字符串（例如'+055.1234'，或者01）
    y = round(float(y), 4)  # 将字符串转换为浮点数据，并四舍五入取4位小数

    # 更新图表
    line.set_data(x,y)  # 设置新的数据
    ax.relim()  # 重新计算轴界限
    ax.autoscale_view()  # 自动调整轴范围
    plt.draw()  # 绘制图表
    plt.pause(0.001)  # 暂停一小段时间，使图表能够更新

# 读取串口数据
# while True:
#     ser.write(b'SR,01,001\r\n')  # 发送指令，
#     receive = ser.readline()  # 接收传感器响应
#     # receive = ser.read_all() # 读取一行数据（以换行符为结束符）
#     y = receive.decode()  # 解码获得字符串
#     y = y.rsplit(",", 1)[1]  # 将字符串拆分，提取右侧第一个字符串（例如'+055.1234'，或者01）
#     y = round(float(y), 4)  # 将字符串转换为浮点数据，并四舍五入取4位小数
#     print(y)

#     plt.plot(  y, color='blue', label='x')
#     plt.xlabel('Time')
#     plt.ylabel('Value')
#     plt.title('y')
#     plt.legend()
#     plt.show()

# 关闭串口连接
ser.close()
    