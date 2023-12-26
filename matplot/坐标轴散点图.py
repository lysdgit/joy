import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建一个3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 生成数据
z = np.random.randn(100)
x = np.random.randn(100)
y = np.random.randn(100)

# 绘制散点图
ax.scatter(x, y, z, c=z, cmap='viridis')

# 添加标签和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot')

# 初始化鼠标事件
ax.mouse_init()

# 定义鼠标滚动事件
def on_scroll(event):
    ax.view_init(elev=ax.elev + event.step, azim=ax.azim)

    # 更新坐标轴显示
    ax.format_coord = lambda x, y: "x={:.3f}, y={:.3f}, z={:.3f}".format(
        ax.get_xlim()[0] + (ax.get_xlim()[1] - ax.get_xlim()[0]) * x / ax.get_window_extent().width,
        ax.get_ylim()[0] + (ax.get_ylim()[1] - ax.get_ylim()[0]) * (ax.get_window_extent().height - y) / ax.get_window_extent().height,
        ax.get_zlim()[0] + (ax.get_zlim()[1] - ax.get_zlim()[0]) * y / ax.get_window_extent().height)

    fig.canvas.draw()

# 绑定鼠标滚动事件
fig.canvas.mpl_connect('scroll_event', on_scroll)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.show()

# 设置坐标轴范围
# ax.set_xlim([-1, 80])
# ax.set_ylim([-2, 80])
# ax.set_zlim([-2, 80])

# # 标出坐标原点
# ax.scatter(0, 0, 0, s=5, color='red')

# # 标出x轴正负
# ax.plot([0, 100], [0, 0], [0, 0], color='black')  # x轴正向
# ax.plot([0, -100], [0, 0], [0, 0], color='gray')  # x轴负向
# ax.text(100, 0, 0, 'x', color='black')  # x轴正向的标签
# ax.text(-100, 0, 0, '-x', color='gray')  # x轴负向的标签

# # 标出y轴正负
# ax.plot([0, 0], [0, 100], [0, 0], color='black')  # y轴正向
# ax.plot([0, 0], [0, -100], [0, 0], color='gray')  # y轴负向
# ax.text(0, 100, 0, 'y', color='black')  # y轴正向的标签
# ax.text(0, -100, 0, '-y', color='gray')  # y轴负向的标签

# # 标出z轴正负
# ax.plot([0, 0], [0, 0], [0, 100], color='black')  # z轴正向
# ax.plot([0, 0], [0, 0], [0, -100], color='gray')  # z轴负向
# ax.text(0, 0, 100, 'z', color='black')  # z轴正向的标签
# ax.text(0, 0, -100, '-z', color='gray')  # z轴负向的标签

# # 生成数据
# z = np.random.randn(10)
# x = np.random.randn(10)
# y = np.random.randn(10)

# # 绘制散点图
# ax.scatter(x, y, z, c=z, cmap='viridis')
# plt.show()
