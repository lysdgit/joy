import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog

# 创建 QApplication 对象
app = QApplication(sys.argv)

# 创建 QWidget 对象
widget = QWidget()

# 设置窗口标题和尺寸
widget.setWindowTitle('My First PyQt5 App')
widget.resize(300, 200)

# 显示窗口
widget.show()

# 运行应用程序的主循环
sys.exit(app.exec_())

class SerialWork(QObject):
    def __init__(self):
        super().__init__()
        self.com = QSerialPort()
        self.com.setPortName('COM1')
        self.com.setBaudRate(9600)
        if self.com.open(QSerialPort.ReadWrite) == False:
            return
        self.readtimer = QTimer()
        self.readtimer.timeout.connect(self.readData)
        self.readtimer.timeout.connect(self.OutPut)
        self.readtimer.start(100)

    def readData(self):
        revData = self.com.readAll()
        revData = bytes(revData)
        if len(revData) > 0:
            #revData = revData.decode()
            # print(revData)
            #revData=revData.split(",")
            data_x = revData[0:6]
            data_x = float(data_x)
            print("run read")
            print(data_x)
            # data_y = revData[7:13]
            # data_y =float(data_y)
            # print(data_y)
            # data_z = revData[14:20]
            # data_z =float(data_z)
            # print(data_z)
            # self.datax=data_x
            # print(type(data_x))
            # print(revData[0:2])
            # print(revData[3:5])
            # print(revData[6:8])
            

    def OutPut(self):
    #     print("hi")
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter(8, 8, 3)
        plt.draw()
        plt.show()
       
 # 创建3D图形对象
        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        # ax.scatter(123, 788, 123)
        # # 刷新图形
        # plt.draw()
        # # plt.pause(1)

        # #  显示图形
        # plt.show()
        #     # print(self.data_x)



class PyQt_Serial(QObject):
    def __init__(self):
        super().__init__()
        self.serialthread = QThread()
        self.serialwork = SerialWork()
        self.serialwork.moveToThread(self.serialthread)
        self.serialthread.started.connect(self.serialwork.init)
        self.serialthread.start()


if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    win = SerialWork()
    sys.exit(app.exec_())



    