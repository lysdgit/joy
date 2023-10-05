import serial
import matplotlib.pyplot as plt

# 设置串口参数
ser = serial.Serial('COM4', 9600)  # 根据实际情况修改串口号和波特率

# 初始化数据列表
x_data = []
y_data = []

# 创建折线图对象
fig, ax = plt.subplots()

# 创建空折线对象
line, = ax.plot([], [])

# 设置坐标轴范围
ax.set_xlim(0, 10)  # 修改 x 轴范围
ax.set_ylim(0, 100)  # 修改 y 轴范围

# 更新函数
def update(data):
    x_data.append(data[0])  # 将新数据添加到 x 数据列表
    y_data.append(data[1])  # 将新数据添加到 y 数据列表

    line.set_data(x_data, y_data)  # 更新折线数据

    # 自动调整坐标轴范围，可以根据需要取消注释
    # ax.relim()
    # ax.autoscale_view()

    plt.pause(0.01)  # 更新绘图并暂停一小段时间

# 实时读取串口数据并绘制折线图
while True:
    try:
        data = ser.readline().decode().strip()  # 读取一行数据并解码
        data = data.split(',')  # 将逗号分隔的字符串转换为浮点数列表

        update(data)  # 更新折线图数据

    except KeyboardInterrupt:
        ser.close()  # 当按下 Ctrl+C 键时关闭串口
        break

# 显示折线图
plt.show()
