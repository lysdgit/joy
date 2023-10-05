


# import numpy as np
# import matplotlib.pyplot as plt
# from pyproj import Proj, transform

# # 定义WGS 84椭球体模型的参数
# a = 6378137  # 赤道半径
# f = 1 / 298.257223563  # 扁率

# # 假设有一组GPS测量数据，包括经度、纬度和高度
# longitude = [63.46,63.51,63.54,63.53]
# latitude = [62.95,63.149,63.28,63.16]
# altitude = [76.86,76.81,76.7,76.759]

# # 将经纬度和高度转换为空间笛卡尔坐标
# in_proj = Proj(init='epsg:4326')
# out_proj = Proj(proj='utm', zone=51, ellps='WGS84')
# x, y, z = transform(in_proj, out_proj, longitude, latitude, altitude)

# # 计算重心点的坐标
# mean_x = np.mean(x)
# mean_y = np.mean(y)
# mean_z = np.mean(z)

# # 计算每个位置与重心点之间的距离
# delta_x = x - mean_x
# delta_y = y - mean_y
# delta_z = z - mean_z
# delta_xyz = np.sqrt(delta_x**2 + delta_y**2 + delta_z**2)

# # 计算位置重复定位精度
# pra = np.mean(delta_xyz)

# # 可视化结果
# plt.scatter(x, y)
# plt.scatter(mean_x, mean_y, c='r', marker='x')
# plt.title('Positioning Repeatable Accuracy: {}'.format(pra))
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
import math


n=15
# 假设有一组GPS测量数据，包括经度、纬度和高度
x = [65.189,65.42,65.41,65.39,65.36,65.42,65.41,65.28,65.4,65.38,65.38,65.42,65.37,65.4,65.259]
y = [69.619,69.63,69.63,69.63,69.619,69.63,69.63,69.63,69.6,69.6,69.59,69.6,69.51,69.6,69.59,]
z = [68.24,68.25,68.25,68.27,68.25,68.229,68.3,68.54,68.28,68.27,68.28,68.289,68.27,68.28,68.27]

# 计算每次测量的平均值
_x = np.mean(x)
_y = np.mean(y)
_z = np.mean(z)

# 计算每次测量与平均值之间的差异度
delta_x = np.abs(x - _x)
delta_y = np.abs(y - _y)
delta_z = np.abs(z - _z)

# 计算位置重复定位精度 L
l = np.sqrt((delta_x**2) + (delta_y**2) + (delta_z**2))

_l=np.mean(l)
sii=sum((l-_l)**2)
si=(sii)/(n-1)
s=math.sqrt(si)
print(s)
print(_l+3*s)
# #到达位置（attained position）距离其重心点距离的平均值
# lavg=np.mean(l)

# sl=(l-lavg)**2


# #标准偏差sl
# n=3
# slsl=(np.sum(sl))/(n-1)

# pc = math.sqrt(slsl)
# pcc=pc/4
# pra=lavg+3*pc

# print(lavg)
# print(sl)
# print(pcc)
# print(lavg+3*pc)

# 可视化结果
# plt.scatter(x, y)
# plt.scatter(mean_x, mean_y, c='r', marker='x')
# plt.title('Positioning Repeatable Accuracy: {}'.format(pra))
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
