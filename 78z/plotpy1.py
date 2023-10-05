from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig = plt.figure()
#创建绘图区域
ax = plt.axes(projection='3d')
# #构建xyz
# x = [63.46, 63.51, 63.54, 63.53]
# y = [62.95, 63.14, 63.28, 63.16]
# z = [76.86, 76.81, 76.72, 76.72]

#限制xyz范围
ax.set_xlim([60, 80])
ax.set_ylim([60, 80])
ax.set_zlim([60, 80])

# 标出x轴正负
ax.plot([60, 80], [0, 0], [0, 0], color='black')  # x轴正向
ax.plot([0, -100], [0, 0], [0, 0], color='gray')  # x轴负向
ax.text(60, 80, 0, 'x', color='black')  # x轴正向的标签
ax.text(-100, 0, 0, '-x', color='gray')  # x轴负向的标签

# 标出y轴正负
ax.plot([0, 0], [60, 80], [0, 0], color='black')  # y轴正向
ax.plot([0, 0], [0, -100], [0, 0], color='gray')  # y轴负向
ax.text(60, 80, 0, 'y', color='black')  # y轴正向的标签
ax.text(0, -100, 0, '-y', color='gray')  # y轴负向的标签

# 标出z轴正负
ax.plot([0, 0], [0, 0], [60, 80], color='black')  # z轴正向
ax.plot([0, 0], [0, 0], [0, -100], color='gray')  # z轴负向
ax.text(0, 60, 80, 'z', color='black')  # z轴正向的标签
ax.text(0, 0, -100, '-z', color='gray')  # z轴负向的标签

# 读取数据
data = pd.read_csv('C:/Users/liys2/Desktop/12.csv')
x = data['x'].values
y = data['y'].values
z = data['z'].values

scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=200)


ax.set_title('3d Scatter plot')
plt.show()