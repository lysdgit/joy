import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# # 生成随机的三维空间坐标
# x = np.random.randn(1000)
# y = np.random.randn(1000)
# z = np.random.randn(1000)

# 读取数据
data = pd.read_csv(r'D:\Project\RRT\LDS-E测试\921\new\2023-08-11-15-07-21 R0.100.csv', skiprows=1, usecols=[0, 1, 2])
x = data['x'].values
y = data['y'].values
z = data['z'].values

# 创建 3x1 的子图
fig, axs = plt.subplots(1, 3, figsize=(18, 8))

# 绘制 xy 平面上的二维分布曲线
axs[0].hist2d(x, y, bins=30, cmap='Blues')
axs[0].set_title('XY Plane')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

# 绘制 xz 平面上的二维分布曲线
axs[1].hist2d(x, z, bins=30, cmap='Blues')
axs[1].set_title('XZ Plane')
axs[1].set_xlabel('x')
axs[1].set_ylabel('z')

# 绘制 yz 平面上的二维分布曲线
axs[2].hist2d(y, z, bins=30, cmap='Blues')
axs[2].set_title('YZ Plane')
axs[2].set_xlabel('y')
axs[2].set_ylabel('z')

#标题
# plt.title('Title')
# 显示图表
plt.show()



# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt

# # 生成随机点坐标
# x = np.random.normal(size=100)
# y = np.random.normal(size=100)

# # 绘制散点图和密度曲线
# sns.jointplot(x=x, y=y, kind='scatter', s=100, edgecolor='w', linewidth=1)
# sns.kdeplot(x=x, y=y, cmap='Reds', shade=True, shade_lowest=False)

# plt.show()
