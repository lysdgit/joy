import sys
import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
import numpy as np
import random
import csv
from datetime import datetime

# 获取当前时间
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# 创建文件名
filename = f'RRT_{current_time}.csv'

class SerialPlotter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowTitle("Serial Plotter")

        # 创建串口对象
        self.serial = serial.Serial()
        self.serial.baudrate = 115200
        #界面选择串口
        self.selected_port = sys.argv[1]
        print("已选择:", self.selected_port)
        self.serial.port = self.selected_port
        #手动选择串口
        # self.serial.port = 'COM3'  # 请根据实际情况修改串口号

        # 创建图形对象
        # self.fig = plt.figure()
        self.fig = plt.figure(figsize=(15, 7),num=' Joyintell ')
        self.ax = self.fig.add_subplot(111, projection='3d')

        # 创建数据列表
        self.x_data = []
        self.y_data = []
        self.z_data = []

        # 创建定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_serial_data)

        # 打开串口连接
        self.serial.open()

        # 启动定时器
        self.timer.start(30)  # 每100毫秒读取一次串口数据

    def read_serial_data(self):
        if self.serial.is_open:
            # 读取串口数据
            line = self.serial.readline().decode().strip()
                # 判断是否为需要舍弃的数据
            if line != '999.990,999.990,999.990':
                # 解析数据
                data = line.split(',')
           
            # float1 = np.round(np.random.uniform(-5, 5), 3)
            # float2 = np.round(np.random.uniform(-5, 5), 3)
            # float3 = np.round(np.random.uniform(-5, 5), 3)
            if len(data) == 3:
                try:
                    x = float(data[0])
                    y = float(data[1])
                    z = float(data[2])

                    # 添加数据到列表
                    self.x_data.append(x)
                    self.y_data.append(y)
                    self.z_data.append(z)

                    data =self.x_data,self.y_data,self.z_data
                    # 创建CSV文件并写入数据
                    with open(filename, 'w', newline='') as file:
                        writer = csv.writer(file)
                        # 写入表头
                        writer.writerow(['芜湖钊晟传感,,'])
                        writer.writerow([current_time,',,'])
                        writer.writerow(['采集点数,,'])
                        writer.writerow([len(self.x_data),',,'])
                        writer.writerow(['x', 'y', 'z'])
                        # 将数据列表转置后写入每一行数据
                        writer.writerows(zip(*data))

                    print(self.x_data)
                    print(self.y_data)
                    print(self.z_data)
                    # 清空图形对象
                    # self.ax.clear()
                    
                    # 设置坐标轴范围
                    self.ax.set_xlim([50, 85])
                    self.ax.set_ylim([50, 85])
                    self.ax.set_zlim([50, 85])

                    # 标出坐标原点
                    x_first = 55
                    y_first = 55
                    z_first = 55
                   
                    # 标出x轴正负
                    self.ax.plot([x_first, x_first+50], [y_first, y_first], [z_first, z_first], color='black')  # x轴正向
                    self.ax.plot([x_first-50, x_first], [y_first, y_first], [z_first, z_first], color='gray')  # x轴负向
                    self.ax.text(x_first+0.01, y_first, z_first, 'X', color='black', fontsize=12)  # x轴正向的标签
                    self.ax.text(-x_first+0.01, y_first, z_first, '-X', color='gray', fontsize=12)  # x轴负向的标签

                    # 标出y轴正负
                    self.ax.plot([x_first, x_first], [y_first, y_first+50], [z_first, z_first], color='black')  # y轴正向
                    self.ax.plot([x_first, x_first], [y_first-50, y_first], [z_first, z_first], color='gray')  # y轴负向
                    self.ax.text(x_first, y_first+0.01, z_first, 'Y', color='black')  # y轴正向的标签
                    self.ax.text(x_first, -y_first+0.01, z_first, '-Y', color='gray')  # y轴负向的标签

                    # 标出z轴正负
                    self.ax.plot([x_first, x_first], [y_first, y_first], [z_first, z_first+50], color='black')  # z轴正向
                    self.ax.plot([x_first, x_first], [y_first, y_first], [z_first-50, z_first], color='gray')  # z轴负向
                    self.ax.text(x_first, y_first, z_first+0.01, 'Z', color='black')  # z轴正向的标签
                    self.ax.text(x_first, y_first, -z_first+0.01, '-Z', color='gray')  # z轴负向的标签

                    # 绘制散点图
                    self.ax.scatter(self.x_data, self.y_data, self.z_data)
                    # 刷新图形
                    plt.draw()
                    plt.pause(0.2)
                    plt.title(len(self.x_data))
                    # plt.show()
                  
                    # self.fig.canvas.draw()

                except ValueError:
                    pass

    def closeEvent(self, event):
        # 停止定时器
        self.timer.stop()

        # 关闭串口连接
        self.serial.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    plotter = SerialPlotter()
    # plotter.show()
    sys.exit(app.exec_())
