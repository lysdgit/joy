import numpy as np
import pandas as pd
from filterpy.kalman import KalmanFilter

# 观测噪声的方差
R = 2

# 系统模型（状态转移矩阵）
A = np.array([[1]])

# 观测模型（测量矩阵）
C = np.array([[1]])

# 初始状态估计
x = np.array([[78.194]])

# 初始协方差矩阵
P = np.array([[1]])

# 存储滤波结果的列表
filtered_data = []

# 温度数据
# measurements = [78.194, 78.195, 78.192, 78.194]
df = pd.read_csv(r'D:\Desk\yhis.csv')
measurements = df['y']
# 对每个测量值进行卡尔曼滤波
for measurement in measurements:
    # 预测步骤
    x_pred = np.dot(A, x)
    P_pred = np.dot(np.dot(A, P), A.T)

    # 更新步骤
    residual = measurement - np.dot(C, x_pred)
    S = np.dot(np.dot(C, P_pred), C.T) + R
    K = np.dot(np.dot(P_pred, C.T), np.linalg.inv(S))
    
    x = x_pred + np.dot(K, residual)
    P = P_pred - np.dot(np.dot(K, C), P_pred)

    filtered_data.append(x[0, 0])

# 输出滤波结果
# for data in filtered_data:
    # print(data)


# 创建DataFrame对象
df = pd.DataFrame(filtered_data, columns=['Filtered Data'])

# 保存DataFrame为CSV文件
df.to_csv('okk.csv', index=False)

print("结果已保存为okk.csv")