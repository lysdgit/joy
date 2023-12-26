import matplotlib.pyplot as plt

# 定义x和y的值
x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = [2, 4, 6, 8, -10, 12, 10, 8, 6, 4, 2]

# 创建画布和坐标系
fig, ax = plt.subplots()

# 绘制x和y的散点图
ax.scatter(x, y)

# 设置x和y轴的范围
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])

# 设置x和y轴的标签
ax.set_xlabel('x')
ax.set_ylabel('y')

# 设置x和y轴的正负半轴
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# 显示图形
plt.show()
