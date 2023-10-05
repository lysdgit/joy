import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建串口对象
ser = serial.Serial('COM10', 115200)  # 替换为你的串口名称和波特率

# 创建3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 读取串口数据并绘制散点图
while True:
    data = ser.readline()  # 读取一行数据（以换行符为结束符）
    print(data)
    # str = data.decode()  # 将字节字符串转换为字符串
    # print(str)  # 打印转换后的字符串
    # x=float(str[0:6])
    # y=float(str[7:13])
    # z=float(str[14:20])
    # print("x =", x)
    # print("y =", y)
    # print("z =", z)
        # data_x = (data[0])
        # data_y = (data[1])
        # data_z = (data[2])
    # data_x = float(data[0])
    # data_y = float(data[1])
    # data_z = float(data[2])
    # print(data_x,data_y,data_z)
   
    # ax.scatter(x, y, z)
    # 刷新图形
    plt.draw()
    plt.pause(1)

# 显示图形
plt.show()