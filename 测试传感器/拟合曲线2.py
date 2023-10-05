import numpy as np
import pandas as pd
# 原始数据
df = pd.read_csv(r'D:\Desk\yhis.csv')
x = df['x']
y = df['y']

# 多项式拟合
coefficients = np.polyfit(x, y, 6)

# 构建多项式方程
polynomial = np.poly1d(coefficients)
equation = polynomial.__str__()

print("多项式方程: ")
print(equation)

