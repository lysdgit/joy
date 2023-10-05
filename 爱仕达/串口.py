import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


# 创建串口对象
ser = serial.Serial('COM5', 9600)  # 替换为你的串口名称和波特率

# 创建3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 读取串口数据并绘制散点图
while True:
    data_raw = ser.readline()  # 读取一行数据（以换行符为结束符）
    data = data_raw[-21:]
    data = data.decode('ascii')
    data_x = float(data[0:6])
    data_y = float(data[7:13])
    data_z = float(data[14:20])
    print(data_x)
    # print(type(data_x))
    # print(data[7:13])
    # print(data[14:20])
    # data_x = float(data[0])
    # data_y = float(data[1])
    # data_z = float(data[2])
    # random_number = random.randint(-10, 10)
    # random_number1 = random.randint(-10, 10)
    # random_number2 = random.randint(-10, 10)
    # ax.scatter(data_x-random_number, data_y+random_number1, data_z+random_number2)
    ax.scatter(data_x, data_y, data_z)
    # 刷新图形
    plt.draw()
    plt.pause(1)

# 显示图形
plt.show()


    # data = data.decode().strip()  # 解码数据并去除首尾的空白字符
    # data = data.split(",")
    
    # print(data[0])
    # print(type(data[0]))