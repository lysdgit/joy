from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QByteArray, QIODevice


# 配置串口参数
serial = QSerialPort()
serial.setPortName("COM5")  # 设置串口名称
serial.setBaudRate(QSerialPort.Baud9600)  # 设置波特率
serial.setDataBits(QSerialPort.Data8)  # 设置数据位
serial.setParity(QSerialPort.NoParity)  # 设置校验位
serial.setStopBits(QSerialPort.OneStop)  # 设置停止位
serial.setFlowControl(QSerialPort.NoFlowControl)  # 设置流控制


def handleReadyRead():
    data = serial.readAll()
    print(data)



serial.close()


