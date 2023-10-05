import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.font_manager import FontProperties
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

# 设置中文字体
font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=22)

class sandian(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("散点图")
        self.select_file()  

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "散点显示", "", "CSV Files (*.csv)", options=options)
        if fileName:
            try:
                #做标题
                # data1 = pd.read_csv(fileName,encoding='GBK',skiprows=3, nrows=1)
                data1 = pd.read_csv(fileName,nrows=1)
                # 转换为字符串
                data1_str = data1.to_string(index=False)
                # 去除"x", "y", "z"
                data1_str = data1_str.replace("x", "").replace("y", "").replace("z", "").replace("r", "").replace("Unnamed: 1", "").replace("Unnamed: 2", "").replace("Unnamed: 3", "")
                # 打印结果
                # print(data1_str)
                #做数据来源
                df = pd.read_csv(fileName, skiprows=1, usecols=[0, 1, 2]) 
                df = df[~(df == 0).all(axis=1)]
            except:
                return
        else:
            return
    
        x_max = df['x'].max()
        x_min = df['x'].min()
        y_max = df['y'].max()
        y_min = df['y'].min()
        z_max = df['z'].max()
        z_min = df['z'].min()   

        # 创建Figure和Axes3D对象
        fig = plt.figure(figsize=(8, 6),num=' JOYINTELL ')
        ax = fig.add_subplot(111, projection='3d')
        
        # 定义鼠标滚轮事件处理函数
        def on_scroll(event):
            axtemp = event.inaxes
            # 判断事件是否发生在图形上
            if axtemp is not None:
                # 判断事件类型是否为鼠标滚轮事件
                if event.button == 'up':
                    # 向上滚动鼠标滚轮，放大图形
                    axtemp.set_xlim(axtemp.get_xlim()[0] * 0.9, axtemp.get_xlim()[1] * 0.9)
                    axtemp.set_ylim(axtemp.get_ylim()[0] * 0.9, axtemp.get_ylim()[1] * 0.9)
                    axtemp.set_zlim(axtemp.get_zlim()[0] * 0.9, axtemp.get_zlim()[1] * 0.9)
                elif event.button == 'down':
                    # 向下滚动鼠标滚轮，缩小图形
                    axtemp.set_xlim(axtemp.get_xlim()[0] * 1.1, axtemp.get_xlim()[1] * 1.1)
                    axtemp.set_ylim(axtemp.get_ylim()[0] * 1.1, axtemp.get_ylim()[1] * 1.1)
                    axtemp.set_zlim(axtemp.get_zlim()[0] * 1.1, axtemp.get_zlim()[1] * 1.1)
            fig.canvas.draw()

        # 连接鼠标滚轮事件
        fig.canvas.mpl_connect('scroll_event', on_scroll)

        # 绘制坐标系
        # ax.plot([0, x_max], [0, 0], [0, 0], 'k-')  # x 轴
        # ax.plot([0, 0], [0, y_max], [0, 0], 'k-')  # y 轴
        # ax.plot([0, 0], [0, 0], [0, z_max], 'k-')  # z 轴

        # 设置坐标轴范围
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.set_zlim([z_min, z_max])

        # 添加坐标轴标签
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # 标出坐标原点
        x_first = df['x'].iloc[0]
        y_first = df['y'].iloc[0]
        z_first = df['z'].iloc[0]
        ax.scatter(x_first, y_first, z_first, s=100, color='red')

        # 标出x轴正负
        ax.plot([x_first, x_first+5], [y_first, y_first], [z_first, z_first], color='black')  # x轴正向
        ax.plot([x_first-5, x_first], [y_first, y_first], [z_first, z_first], color='gray')  # x轴负向
        ax.text(x_first+0.01, y_first, z_first, 'X', color='black', fontsize=12)  # x轴正向的标签
        ax.text(-x_first+0.01, y_first, z_first, '-X', color='gray', fontsize=12)  # x轴负向的标签

        # 标出y轴正负
        ax.plot([x_first, x_first], [y_first, y_first+5], [z_first, z_first], color='black')  # y轴正向
        ax.plot([x_first, x_first], [y_first-5, y_first], [z_first, z_first], color='gray')  # y轴负向
        ax.text(x_first, y_first+0.01, z_first, 'Y', color='black')  # y轴正向的标签
        ax.text(x_first, -y_first+0.01, z_first, '-Y', color='gray')  # y轴负向的标签

        # 标出z轴正负
        ax.plot([x_first, x_first], [y_first, y_first], [z_first, z_first+5], color='black')  # z轴正向
        ax.plot([x_first, x_first], [y_first, y_first], [z_first-5, z_first], color='gray')  # z轴负向
        ax.text(x_first, y_first, z_first+0.01, 'Z', color='black')  # z轴正向的标签
        ax.text(x_first, y_first, -z_first+0.01, '-Z', color='gray')  # z轴负向的标签

        # 绘制三维点
        x = df['x']
        y = df['y']
        z = df['z']
        ax.scatter(x, y, z, c='b')

        ax.view_init(elev=25, azim=30) #将 3D 坐标轴的方向改为了上下倾斜 45 度，左右旋转 30 度。
        # plt.title('三维坐标散点分布', fontproperties=font)
        plt.title(data1_str, fontproperties=font)
        plt.show()

class zhexian(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("折线图")
        self.open_csv_file()

    def open_csv_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "折线显示", "", "CSV Files (*.csv)", options=options)
        if fileName:
            try:
                #做标题
                data1 = pd.read_csv(fileName,nrows=1)
                # 转换为字符串
                data1_str = data1.to_string(index=False)
                # 去除"x", "y", "z"
                data1_str = data1_str.replace("x", "").replace("y", "").replace("z", "").replace("r", "").replace("Unnamed: 1", "").replace("Unnamed: 2", "").replace("Unnamed: 3", "")
                data = pd.read_csv(fileName, skiprows=1, encoding='GBK', usecols=[0, 1, 2]) 
                data = data[~(data == 0).all(axis=1)]   
            except:
                return
        else:
            return
        
        x = data['x'].values-data['x'].iloc[0]
        y = data['y'].values-data['y'].iloc[0]
        z = data['z'].values-data['z'].iloc[0]      

        xmin = float(x.min())
        xmax = float(x.max())
        ymin = float(y.min())
        ymax = float(y.max())
        zmin = float(z.min())
        zmax = float(z.max())
        minaxis = min(xmin, ymin, zmin)
        maxaxis = max(abs(xmax), abs(ymax), abs(zmax))
        l = len(x)
        h = pd.Series(range(1, l+1))

        # 绘制折线图
        plt.figure(figsize=(12, 6), num='JOYINTELL')
        plt.plot(h, x, label='x', color="red")
        plt.plot(h, y, label='y', color="black")
        plt.plot(h, z, label='z', color="blue")
        plt.grid(True)
        plt.xticks(range(min(h), max(h)+1, 1))
        y_ticks = np.arange(minaxis-0.02, maxaxis+0.02, 0.01) #(下限 上限 刻度)
        plt.yticks(y_ticks)
        
        # 添加图例和标签
        plt.legend()
        plt.xlabel('次数',fontproperties=font)
        plt.ylabel('距离差值',fontproperties=font)
        plt.title(data1_str,fontproperties=font)

        # 显示图像
        plt.show()

class MainMenu(QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.setFixedSize(400, 300)
        self.setWindowTitle("芜湖钊晟智能科技")
        layout = QHBoxLayout()
        #layout = QVBoxLayout()

        self.calendar_button = QPushButton("三维散点图")
        font = self.calendar_button.font()
        font.setPointSize(22)
        self.calendar_button.setFont(font)
        self.calendar_button.clicked.connect(self.open_calendar_menu)
        layout.addWidget(self.calendar_button)

        self.time_button = QPushButton("二维折线图")
        font = self.time_button.font()
        font.setPointSize(22)
        self.time_button.setFont(font)
        self.time_button.clicked.connect(self.open_time_menu)
        layout.addWidget(self.time_button)
        
        self.web_button = QPushButton('官网', self)
        font = self.web_button.font()
        font.setPointSize(20)
        self.web_button.setFont(font)
        self.web_button.clicked.connect(self.openUrl)
        self.web_button.setGeometry(150, 50, 100, 40)

        self.setLayout(layout)
        
        # 居中显示窗口
        screen_geometry = QApplication.desktop().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())

    def openUrl(self):
        url = QUrl('http://www.joyintell.com/')
        QDesktopServices.openUrl(url)

    def open_calendar_menu(self):
        self.hide()
        calendar_menu.show()
        sandian()

    def open_time_menu(self):
        self.hide()
        time_menu.show()
        zhexian()

class CalendarMenu(QWidget):
    def __init__(self, parent=None):
        super(CalendarMenu, self).__init__(parent)
        self.setFixedSize(400, 180)
        self.setWindowTitle("三维散点图")
        layout = QVBoxLayout()
        self.back_button = QPushButton("返回")
        font = self.back_button.font()
        font.setPointSize(16)
        self.back_button.setFont(font)
        self.back_button.clicked.connect(self.back_to_main_menu)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def back_to_main_menu(self):
        self.hide()
        main_menu.show()

class TimeMenu(QWidget):
    def __init__(self, parent=None):
        super(TimeMenu, self).__init__(parent)
        self.setFixedSize(400, 180)
        self.setWindowTitle("二维折线图")
        layout = QVBoxLayout()
        self.back_button = QPushButton("返回")
        font = self.back_button.font()
        font.setPointSize(16)
        self.back_button.setFont(font)
        self.back_button.clicked.connect(self.back_to_main_menu)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
    
    def back_to_main_menu(self):
        self.hide()
        main_menu.show()

if __name__ == "__main__":
    app = QApplication([])
    main_menu = MainMenu()
    calendar_menu = CalendarMenu()
    time_menu = TimeMenu()
    main_menu.setWindowIcon(QIcon('C:/Users/liys2/Desktop/pyRD/QT5/joytell.png'))
    main_menu.show()
    app.exec_()
