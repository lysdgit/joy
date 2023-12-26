import serial
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
import numpy as np

# 设置串口参数
ser = serial.Serial('COM1', 115200)  # 根据实际情况修改串口号和波特率
# 十六进制数据
hex_data = bytes.fromhex('FE F0 03 01 00 00 00 00')

# 初始化数据列表
x_data = []
y_data = []

# 创建图形应用程序对象
app = QApplication([])

# 创建窗口和布局
win = QWidget()
layout = QVBoxLayout()
win.setLayout(layout)

# 创建 PlotWidget 对象
pw_x = pg.PlotWidget()
pw_x.setTitle("x轴", color='#000000', size='12pt')
pw_x.setBackground('w')
pw_x.setLabel('left', color='#000000')
pw_x.setXRange(0, 25)
pw_x.setYRange(70, 80)
pw_x.showGrid(x=True, y=True)  # 显示网格线
pw_x.setLabel('left', units='y')
# pw_x.getAxis('left').setTicks([[(tick, f'{tick:.1f}') for tick in np.arange(70, 80, 0.1)]])#y轴步距
layout.addWidget(pw_x)
pw_x.setYRange(70, 100)

# 创建曲线对象
curve_x = pw_x.plot(pen='b')

# 更新函数
def update():
    while True:
        try:
        # 发送数据到串口
            ser.write(hex_data)

        # 读取串口返回的数据
            response = ser.read(10)  # 根据实际情况指定读取的字节数

            if response:
                # 将返回值转换为十六进制字符串，并打印出来
                hex_response = ' '.join(['{:02X}'.format(byte) for byte in response])
                # print('Response:', hex_response)
                # 拆分数据字符串
                data_list = hex_response.split(" ")
                # print(data_list)

                # 获取右六位数据
                right_six = data_list[-3:]
                # print(right_six)

                zhengshu = int(right_six[0] , 16)
                zhengshu_str = str(zhengshu)

                xiaoshu = ''.join([str(right_six[1]), str(right_six[2])])
                xiaoshu = int(xiaoshu,16)
                xiaoshu_str = str(xiaoshu)
                now_data = zhengshu_str+"."+xiaoshu_str
                print(now_data)
                y = float(now_data)
                    
                x_data.append(len(x_data))  # 使用数据列表长度作为 x 值
                y_data.append(y)
                
                curve_x.setData(x_data, y_data)

        except serial.SerialException as e:
            print('Serial Port Error:', str(e))

# 创建定时器，每隔一段时间调用更新函数
timer = QTimer()
timer.timeout.connect(update)
timer.start(20)  # 每200毫秒更新一次

# 显示窗口
win.show()

# 运行应用程序
app.exec_()
