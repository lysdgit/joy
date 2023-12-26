import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def exponential_moving_average(data, alpha):
    ema = [data[0]]
    for i in range(1, len(data)):
        ema.append(alpha * data[i] + (1 - alpha) * ema[i - 1])
    return ema

# 原始数据
# raw_data = [98.7797, 98.7758, 98.7781, 98.7722, 98.7813, 98.7713, 98.769, 98.7704, 98.7798, 98.7772,
#             98.7788, 98.7762, 98.7779, 98.7824, 98.7822, 98.7753, 98.7785, 98.7833, 98.7793, 98.7791,
#             98.7787, 98.7749, 98.7791, 98.7737, 98.7738]

# 从CSV文件读取数据
df = pd.read_csv(r"C:\Users\liys2\Desktop\pyRD\测试传感器\data\98.csv")  # 替换 'your_file.csv' 为你的文件路径

# 提取测距数据列
raw_data = df['dis'].tolist()

# 设置平滑系数，可以根据实际情况调整，一般取值在(0, 1)之间
alpha = 0.2

# 应用指数加权移动平均滤波
filtered_data_ema = exponential_moving_average(raw_data, alpha)

# 绘制原始数据和滤波后的数据的折线图
plt.plot(raw_data, label='原始数据')
plt.plot(filtered_data_ema, label='滤波后数据 (EMA)')

# 添加标签和标题
plt.xlabel('样本序号')
plt.ylabel('测距数值')
plt.title('原始数据和指数加权移动平均滤波后数据的折线图')

# 添加图例
plt.legend()

# 显示图形
plt.show()
