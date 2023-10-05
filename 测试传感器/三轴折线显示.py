import serial
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
import numpy as np

# 设置串口参数
ser = serial.Serial('COM1', 115200)  # 根据实际情况修改串口号和波特率

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
    data = ser.readline().decode().strip()
    print(data)
    # ser.write(b'SR,01,001\r\n')  # 发送指令，
    # 读取串口数据并解码
    # data = ser.readline().decode().rsplit(",", 1)[1] 
    
    y = float(data)  # 将字符串转换为浮点数
    y = round(float(y), 3)  # 将字符串转换为浮点数据，并四舍五入取2位小数
        
    x_data.append(len(x_data))  # 使用数据列表长度作为 x 值
    y_data.append(y)
    
    curve_x.setData(x_data, y_data)

# 创建定时器，每隔一段时间调用更新函数
timer = QTimer()
timer.timeout.connect(update)
timer.start(200)  # 每200毫秒更新一次

# 显示窗口
win.show()

# 运行应用程序
app.exec_()
