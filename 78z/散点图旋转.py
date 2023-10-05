import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 生成随机三维数据
x = np.random.randn(10)
y = np.random.randn(10)
z = np.random.randn(10)

# 创建绘图窗口和三维坐标系
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 初始化绘图
scatter = ax.scatter(x, y, z)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

# 定义更新函数
def update(frame):
    # 计算旋转角度
    angle = frame / 80 * 2 * np.pi
    cos = np.cos(angle)
    sin = np.sin(angle)
    # 旋转坐标系
    ax.view_init(elev=30, azim=frame)
    # 更新散点图数据
    scatter._offsets3d = (x * cos - y * sin, x * sin + y * cos, z)
    # 返回散点图对象
    return scatter,

# 创建动画对象
ani = FuncAnimation(fig, update, frames=100, interval=50)

# 显示动画
plt.show()
