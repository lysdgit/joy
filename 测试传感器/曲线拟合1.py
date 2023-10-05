import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def func(x):
    return -9E-22 * x**6 + 3E-17 * x**5 - 1E-13 * x**4 + 1E-10 * x**3 + 6E-8 * x**2 - 0.0002 * x + 82.855

# 定义绘制图表的范围
x = np.linspace(0, 2500, 3000)  # x 的范围从 -10 到 10，生成 100 个点
y = func(x)

# 绘制图表
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function: y = -9E-22x^6 + 3E-17x^5 - 1E-13x^4 + 1E-10x^3 + 6E-8x^2 - 0.0002x + 82.855')
plt.grid(True)
plt.show()
