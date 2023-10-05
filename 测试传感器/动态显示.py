import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 设置串口参数
ser = serial.Serial('COM1', 9600)  # 根据实际情况修改串口号和波特率

# 初始化数据列表
x_data = []
y_data = []

# 创建折线图对象
fig, ax = plt.subplots()

# 创建空折线对象
line, = ax.plot([], [])

# 设置坐标轴范围
ax.set_xlim(0, 1000)  # 修改 x 轴范围
ax.set_ylim(35, 55)  # 修改 y 轴范围

# 更新函数
def update(frame):
    # 读取串口数据并解码
    data = ser.readline().decode().rsplit(",", 1)[1] 
    y = float(data)  # 将字符串转换为浮点数
    y = round(float(y), 2)  # 将字符串转换为浮点数据，并四舍五入取2位小数

    x_data.append(frame)  # 将新的 x 值添加到 x 数据列表
    y_data.append(y)  # 将新的 y 值添加到 y 数据列表

    line.set_data(x_data, y_data)  # 更新折线数据
    
    # plt.yticks(range(35,55, 0.1))
# 创建动画
ani = FuncAnimation(fig, update, frames=np.arange(0, 1000), interval=200, repeat=False)


# 显示折线图
plt.show()

