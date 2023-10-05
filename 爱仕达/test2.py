import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, QByteArray
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class SerialPlotter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Plotter")
        self.setGeometry(100, 100, 800, 600)

        self.serial_port = QSerialPort()
        self.serial_port.setPortName("COM1")  # 设置串口号
        self.serial_port.setBaudRate(QSerialPort.Baud9600)  # 设置波特率
        self.serial_port.setDataBits(QSerialPort.Data8)  # 设置数据位
        self.serial_port.setParity(QSerialPort.NoParity)  # 设置校验位
        self.serial_port.setStopBits(QSerialPort.OneStop)  # 设置停止位

        self.serial_port.readyRead.connect(self.read_data)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

    def read_data(self):
        while self.serial_port.bytesAvailable() > 0:
            data = self.serial_port.readAll()
            # 处理数据
            # ...
            print(data)
            # 将数据添加到散点图中
            x = 1
            y = 2
            z = 3
            self.ax.scatter(x, y, z)

            self.fig.canvas.draw()

    def start_reading(self):
        if not self.serial_port.isOpen():
            self.serial_port.open(QIODevice.ReadOnly)

    def stop_reading(self):
        if self.serial_port.isOpen():
            self.serial_port.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    serial_plotter = SerialPlotter()
    serial_plotter.show()

    serial_plotter.start_reading()

    sys.exit(app.exec_())
