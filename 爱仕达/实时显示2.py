import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建串口对象
ser = serial.Serial('COM17', 115200)  # 根据实际情况修改串口号和波特率

# 创建3D图形窗口
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 初始化数据列表
x_data = []
y_data = []
z_data = []

# 创建3D散点图对象
scatter = ax.scatter(x_data, y_data, z_data)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 设置坐标轴范围
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_zlim(0, 100)

# 实时更新数据函数
def update_data():
    # 读取串口数据
    data = ser.readline().decode().rstrip()  # 根据实际情况进行解码和处理

    # 解析数据并更新数据列表
    x, y, z = map(float, data.split(','))  # 假设数据格式为"x,y,z"
    x_data.append(x)
    y_data.append(y)
    z_data.append(z)

    # 更新散点图数据
    scatter._offsets3d = (x_data, y_data, z_data)

    # 重新绘制图形
    fig.canvas.draw()

# 主循环
while True:
    update_data()
