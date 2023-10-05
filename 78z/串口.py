import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ser = serial.Serial('COM1', 9600)
# 创建3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 读取串口数据
while True:
    data_raw = ser.readline()  # 读取一行数据（以换行符为结束符）
    str_xyz = data_raw.decode().strip()  # 将字节字符串转换为字符串
    # print(str_xyz)
    xyz= str_xyz.split(",")

    # print(xyz)  # 打印转换后的字符串
    # print(type(xyz))
    x=str_xyz[0:6]
    y=str_xyz[7:13]
    z=str_xyz[14:20]
    print(x,y,z)
    ax.scatter(x,y,z)
    # 刷新图形
    plt.draw()
    # plt.pause(1)

# 显示图形
    plt.show()


    
else:
    print("数据格式不符合要求")


# 关闭串口连接
ser.close()

