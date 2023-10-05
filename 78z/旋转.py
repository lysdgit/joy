import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 创建一个 Figure 对象和一个 Axes 对象
fig, ax = plt.subplots()

# 定义一个空的 Line2D 对象
line, = ax.plot([], [], lw=2)

# 定义动画函数
def animate(i):
    # 计算杆的坐标
    x = np.array([0, np.cos(i), np.cos(i) + 1])
    y = np.array([0, np.sin(i), np.sin(i)])
    
    # 更新 Line2D 对象的坐标
    line.set_data(x, y)
    
    return line,

# 定义动画对象
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 100), interval=50)

# 显示动画
plt.show()
