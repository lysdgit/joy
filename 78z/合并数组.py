import numpy as np

# 创建两个二维数组
data1 = np.random.randn(2, 2)
data2 = np.random.randn(3, 2)

# 将两个数组在垂直方向上合并
X = np.vstack((data1, data2))

print(X)
print(X.shape)  # 输出合并后数组的形状