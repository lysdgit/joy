import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ser = serial.Serial('COM1', 9600)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 读取串口数据
while True:
        x_data = []
        y_data = []
        z_data = []
        line = ser.readline().decode().strip()
        data = line.split(',')

        if len(data) == 3:
            try:
                x = float(data[0])
                y = float(data[1])
                z = float(data[2])

                # 添加数据到列表
                # x_data.append(x)
                # y_data.append(y)
                # z_data.append(z)
                x_data =x
                y_data=y
                z_data =z

                print(x_data)
                print(y_data)
                print(z_data)
                # 清空图形对象
                ax.clear()

                # 设置坐标轴范围
                ax.set_xlim([55, 85])
                ax.set_ylim([55, 85])
                ax.set_zlim([55, 85])

                # 标出坐标原点
                x_first = 55
                y_first = 55
                z_first = 55
                
                # 标出x轴正负
                ax.plot([x_first, x_first+50], [y_first, y_first], [z_first, z_first], color='black')  # x轴正向
                ax.plot([x_first-50, x_first], [y_first, y_first], [z_first, z_first], color='gray')  # x轴负向
                ax.text(x_first+0.01, y_first, z_first, 'X', color='black', fontsize=12)  # x轴正向的标签
                ax.text(-x_first+0.01, y_first, z_first, '-X', color='gray', fontsize=12)  # x轴负向的标签

                # 标出y轴正负
                ax.plot([x_first, x_first], [y_first, y_first+50], [z_first, z_first], color='black')  # y轴正向
                ax.plot([x_first, x_first], [y_first-50, y_first], [z_first, z_first], color='gray')  # y轴负向
                ax.text(x_first, y_first+0.01, z_first, 'Y', color='black')  # y轴正向的标签
                ax.text(x_first, -y_first+0.01, z_first, '-Y', color='gray')  # y轴负向的标签

                # 标出z轴正负
                ax.plot([x_first, x_first], [y_first, y_first], [z_first, z_first+50], color='black')  # z轴正向
                ax.plot([x_first, x_first], [y_first, y_first], [z_first-50, z_first], color='gray')  # z轴负向
                ax.text(x_first, y_first, z_first+0.01, 'Z', color='black')  # z轴正向的标签
                ax.text(x_first, y_first, -z_first+0.01, '-Z', color='gray')  # z轴负向的标签

                # 绘制散点图
                colors = x_data
                # colors = np.linspace(0, 100, 100)
                ax.scatter(x_data, y_data, z_data, c=colors)
                # ax.scatter(x_data, y_data, z_data,c=colors, cmap='cool')

                # 刷新图形
                plt.draw()
                plt.pause(0.1)
                # plt.title(len(x_data))
                plt.show()

            except ValueError:
                    pass


# 关闭串口连接
ser.close()