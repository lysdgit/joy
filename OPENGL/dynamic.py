import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# 创建一个空的图形对象
fig, ax = plt.subplots()
# 创建一个空的曲线对象
line, = ax.plot([], [], lw=2)
# 设置坐标轴范围
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
# 设置坐标轴标签
ax.set_xlabel('Time')
ax.set_ylabel('Value')

# 生成随机数据
x_data = 30*(np.random.rand(10))+50
# # y_data = np.sin(x_data)-1
y_data = 60*(np.random.rand(10))+30*(np.random.rand(10))


# 记录数值的变化历史
x_history = []
y_history = []

# 更新函数，用于更新曲线的数据
def update(i):
    x = x_data[i]
    y = y_data[i]
    x_history.append(x)
    y_history.append(y)
    line.set_data(x_history, y_history)
    return line,

# 动态绘制曲线
ani = animation.FuncAnimation(fig, update, frames=len(x_data), interval=100, blit=True)

# 显示动态曲线
plt.show()
