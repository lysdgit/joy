import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from readnum import readdis  # 假设你的模块为readnum，且包含readdis函数


# 创建一个图形窗口和坐标轴
fig, ax = plt.subplots()
x_data = []
y_data = []

# 创建一个空的 plot 对象，用于更新数据
line, = ax.plot([], [], marker='o', linestyle='-', color='b')

# 设置坐标轴标签和标题
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Real-time Data Visualization')

# 定义更新数据的函数
def update(frame):
    result_str = readdis(6, 115200, 2, 0.5)  # 假设readdis返回一个字符串
    result_float = float(result_str)  # 将字符串转换为浮点数
    print(result_float)
    if result_float != '255.0':
        x_data.append(frame)
        y_data.append(result_float)

        # 更新 plot 对象的数据
        line.set_data(x_data, y_data)

        # 调整坐标轴范围（可选）
        ax.relim()
        # ax.set_ylim(80, 110)
        ax.autoscale_view()

        return line,

# 创建动画
animation = FuncAnimation(fig, update, frames=range(1000), interval=0.01)

# 显示图形窗口
plt.show()
