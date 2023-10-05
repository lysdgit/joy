import serial
import sys
import struct
import serial.tools.list_ports
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from chuankou import *


########################
#函数区
####################################################
# 串口函数区
def get_com_list():
    Com_List = []
    plist = list(serial.tools.list_ports.comports())
    if len(plist) > 0:
        for i in range(len(plist)):
            Com_List.append(list(plist[i])[0])
    print(Com_List) 
    return Com_List

#####################################################

#创建主界面
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('serialscope.ico'))
        self.sendbutton.setToolTip('点击打开串口')
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.time_out)
    def time_out(self):
            global ser, timer_value
            data = ser.read_all()
            print(data)
            if data != b'':
                data = data.decode('utf-8')
                self.recvddata.append(data)
            self.timer.start(timer_value)

    #######################
    def open_com(self):
        global ser, serialPort, baudRate, com_list
        com_list = get_com_list()
        if com_list != []: 
            if serialPort != None:
                ser.port = serialPort
                ser.baudrate = baudRate
                if self.sendbutton.text() == '连接':
                    ser.open() 
                    self.timer.start(timer_value) 
                    self.sendbutton.setText("关闭")
                    self.sendbutton.setToolTip('点击关闭串口')
                    print('串口已连接')
                else:
                    self.timer.stop()
                    ser.close()
                    self.sendbutton.setText("连接")
                    self.sendbutton.setToolTip('点击打开串口')
                    print('串口已断开')
            else: 
                myWin.port_combo.clear()
                for i in range(len(com_list)):
                    myWin.sendcom.addItem(com_list[i])
                serialPort = com_list[0]
        else: 
            serialPort = None
            myWin.sendcom.clear()
            myWin.show_dialog(str='请先打开串口')
   #向串口发送数据
    def senddatatocom(self):
        global serialPort, ser
        if self.sendbutton.text() == '关闭'and serialPort != None:
            send_str=self.inputdata.toPlainText()
            state_checknline=self.checknline.isChecked()
            if state_checknline == True:
                print('发送新行')
                send_str += '\r\n'
            ser.write(send_str.encode('utf-8'))
            print('发送数据为：'+send_str)
        else:
            self.show_dialog(str='请先打开串口')
    def port_changed(self, text):
        global serialPort
        serialPort = text
        print('串口：' + serialPort)
        ser.port = serialPort
    def baud_changed(self, text):
        global baudRate
        baudRate = int(text)
        print(baudRate)
        ser.baudrate=baudRate
####################################################
#全局变量及先行代码
app = QApplication(sys.argv)
myWin = MyWindow()
myWin.show()
baudRate = 115200 
timer_value=100
#################################################
ser=serial.Serial(timeout=0.5)
com_list=get_com_list() 
if com_list!=[]:
    for i in range(len(com_list)): 
        myWin.sendcom.addItem(com_list[i])
    serialPort = com_list[0] 
else:
    serialPort = None
    myWin.show_dialog(str='请先打开串口')


sys.exit(app.exec_())