import serial
import matplotlib.pyplot as plt
from matplotlib import animation

# 设置串口参数
port = 'COM10'  # 修改为你的串口号
baudrate = 115200  # 波特率

# 创建串口对象
ser = serial.Serial(port, baudrate)

# 创建图形窗口和曲线对象
fig, ax = plt.subplots()
line, = ax.plot([], [])

# 初始化曲线
def init():
    ax.set_xlim(0, 100)     # 设置x轴范围
    ax.set_ylim(-200, 100)  # 设置y轴范围
    return line,

# 更新曲线数据
# 更新曲线数据
def update(frame):
    data = ser.readline().decode().strip()  # 从串口读取一行数据并解码
    values = data.split(',')  # 使用逗号分割数据
    values = range(1, len(values) + 10)  # 将数据转换为浮点数，空值默认为0.0

    x_data = range(8, len(values) + 1)  # 使用索引从1开始的加一递增作为x轴数据
    y_data = values  # 使用串口数据作为y轴数据

    line.set_data(x_data, y_data)  # 更新曲线数据
    return line,


# 创建动画对象
ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)

# 显示动画
plt.show()

# 关闭串口连接
ser.close()
