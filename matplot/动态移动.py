from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# 创建3D图形对象
fig = plt.figure()
ax = plt.axes(projection='3d')

# 创建空间路径数据
x1 = np.random.randn(50)*50
y1 = np.random.randn(50)*70
z1 = np.random.randn(50)*81

# x2 = np.linspace(2, 3, 50)
# y2 = np.linspace(2, 3, 50)
# z2 = np.linspace(2, 3, 50)

# 绘制三个点
# ax.scatter3D(1, 1, 1, color='red', label='a')
# ax.scatter3D(2, 2, 2, color='green', label='b')
# ax.scatter3D(3, 3, 3, color='blue', label='c')

# 绘制三个点的移动过程
for i in range(50):
    ax.scatter3D(x1[i], y1[i], z1[i], color='red')
    # ax.scatter3D(x2[i], y2[i], z2[i], color='green')
    # ax.scatter3D(3, 3, 3, color='blue')
    plt.pause(0.01)

# 设置坐标轴标签和图例
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# 显示图形
plt.show()
