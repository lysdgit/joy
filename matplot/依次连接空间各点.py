import matplotlib.pyplot as plt
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D

# 初始化数据
x = [65.189,65.42,65.41,65.39,65.36,65.42,65.41,65.28,65.4,65.38,65.38,65.42,65.37,65.4,65.259]
y = [69.619,69.63,69.63,69.63,69.619,69.63,69.63,69.63,69.6,69.6,69.59,69.6,69.51,69.6,69.59,]
z = [68.24,68.25,68.25,68.27,68.25,68.229,68.3,68.54,68.28,68.27,68.28,68.289,68.27,68.28,68.27]
#df = pd.read_csv('C:/Users/liys2/Desktop/12.csv', skiprows=3)
# df = pd.read_csv('C:/Users/liys2/Desktop/12.csv')
# df = pd.read_csv(r'C:\Users\liys2\Desktop\822\2023-08-22-11-48-31.csv', skiprows=1, usecols=[0, 1, 2])
# x = df['x']
# y = df['y']
# z = df['z']

# 创建3D图形对象
fig = plt.figure(figsize=(13, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图和路径
for i in range(len(x)):
    ax.scatter(x[i], y[i], z[i], c='r', marker='o')
    ax.text(x[i], y[i], z[i], str(i+1), color='black', fontsize=12)
if len(x) > 1:
    ax.plot(x, y, z, c='b')

# 设置坐标轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 显示图形
plt.show()
