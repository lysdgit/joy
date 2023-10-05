import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建图形和坐标系
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.gcf().subplots_adjust(left=None,top=None,bottom=None, right=None)

# 绘制坐标系
ax.plot([0, 1], [0, 0], [0, 0], 'k-')  # x 轴
ax.plot([0, 0], [0, 1], [0, 0], 'k-')  # y 轴
ax.plot([0, 0], [0, 0], [0, 1], 'k-')  # z 轴

# 设置坐标轴范围
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# 添加坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()
