import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math
from tkinter import *
from tkinter import ttk
# 设置中文字体
font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=22)

def open_calculator():
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            # 获取屏幕的宽度和高度
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            # 设置窗口的宽度和高度
            window_width = 400
            window_height = 300
            # 计算窗口的位置
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            # 设置窗口的位置 
            root.geometry(f"{window_width}x{window_height}+{x}+{y}")
            # self.master.geometry('400x300')
            self.pack()
            self.create_widgets()
    
        def create_widgets(self):
            self.master.title("芜湖钊晟")
            self.select_file_button = tk.Button(self, font=('Arial', 22))  # 设置按钮字体大小为16
            self.select_file_button["text"] = "选择CSV文件"
            self.select_file_button["command"] = self.select_file
            self.select_file_button.pack(side="top", pady=100)  # 设置按钮上下间距

        def select_file(self):
            # 打开文件选择对话框
            file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

            # 从CSV文件中读取点数据
            df = pd.read_csv(file_path, skiprows=4, encoding='GBK', usecols=[0, 1, 2])

            x_max = df['x'].max()
            x_min = df['x'].min()
            y_max = df['y'].max()
            y_min = df['y'].min()
            z_max = df['z'].max()
            z_min = df['z'].min()   

            # 创建Figure和Axes3D对象
            fig = plt.figure(figsize=(8, 6),num=' JoySens ')
            ax = fig.add_subplot(111, projection='3d')

            # 绘制坐标系
            # ax.plot([0, x_max], [0, 0], [0, 0], 'k-')  # x 轴
            # ax.plot([0, 0], [0, y_max], [0, 0], 'k-')  # y 轴
            # ax.plot([0, 0], [0, 0], [0, z_max], 'k-')  # z 轴

            # 设置坐标轴范围
            ax.set_xlim([x_min, x_max])
            ax.set_ylim([y_min, y_max])
            ax.set_zlim([z_min, z_max])

            # 设置旋转时旋转坐标轴和画布
            # ax.view_init(elev=30, azim=45)
            
            # 添加坐标轴标签
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')

            # 绘制三维坐标轴
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            # 标出坐标原点
            ax.scatter(0, 0, 0, s=30, color='red')
            # 标出x轴正负
            ax.plot([0, 10], [0, 0], [0, 0], color='black')  # x轴正向
            ax.plot([0, -10], [0, 0], [0, 0], color='gray')  # x轴负向
            ax.text(0.5, 0, 0, 'x', color='black')  # x轴正向的标签
            ax.text(-0.5, 0, 0, '-x', color='gray')  # x轴负向的标签

            # 标出y轴正负
            ax.plot([0, 0], [0, 10], [0, 0], color='black')  # y轴正向
            ax.plot([0, 0], [0, -10], [0, 0], color='gray')  # y轴负向
            ax.text(0, 0.5, 0, 'y', color='black')  # y轴正向的标签
            ax.text(0, -0.5, 0, '-y', color='gray')  # y轴负向的标签

            # 标出z轴正负
            ax.plot([0, 0], [0, 0], [0, 10], color='black')  # z轴正向
            ax.plot([0, 0], [0, 0], [0, -10], color='gray')  # z轴负向
            ax.text(0, 0, 0.5, 'z', color='black')  # z轴正向的标签
            ax.text(0, 0, -0.5, '-z', color='gray')  # z轴负向的标签

            # 绘制三维点
            x = df['x']
            y = df['y']
            z = df['z']
            ax.scatter(x, y, z, c='k')
            # ax.grid(True)
            ax.view_init(elev=20, azim=45) #将 3D 坐标轴的方向改为了上下倾斜 45 度，左右旋转 30 度。
            # plt.title('Positioning Repeatable Accuracy: {}'.format(pra))
            plt.title('三维坐标', fontproperties=font)
            plt.show()
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


def open_unit_converter():
    # 创建Tkinter窗口
    window = tk.Tk()
    window.title("折线图")
    # window.geometry("400x300")  # 设置窗口大小为400*300
    # 设置窗口的宽度和高度
    window_width = 400
    window_height = 300

    # 获取屏幕的宽度和高度
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # 计算窗口的初始位置
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    # 设置窗口的位置和大小
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 创建回调函数，用于选择CSV文件并读取数据
    def open_file():
    # 弹出文件选择对话框
        file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        
        # 读取数据
        data = pd.read_csv(file_path)
        
        # 舍去全为0的一行
        data = data[~(data == 0).all(axis=1)]
        
        x = data['x'].values
        y = data['y'].values
        z = data['z'].values
        
        xmin = int(x.min())
        xmax = int(x.min())
        ymin = int(y.min())
        ymax = int(y.max())
        zmin = int(z.min())
        zmax = int(z.max())
        minaxis = min(xmin, ymin, zmin)
        maxaxis = max(xmax, ymax, zmax)
        
        l = len(x)
        h = pd.Series(range(1, l+1))
        
        # 绘制折线图
        plt.figure(figsize=(12, 6), num='JoySens')
        plt.plot(h, x, label='x', color="red")
        plt.plot(h, y, label='y', color="black")
        plt.plot(h, z, label='z', color="blue")
        plt.grid(True)
        plt.xticks(range(min(h), max(h)+1, 1))
        plt.yticks(range(minaxis, maxaxis+2, 1))
        
        # 添加图例和标签
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('77777')
        
        # 显示图像
        plt.show()

    # 创建按钮，点击按钮选择CSV文件并读取数据
    style = ttk.Style()
    style.configure("TButton", borderwidth=0, padding=6, relief="flat", background="#ccc", font=("Arial", 22), bordercolor="#ccc", borderradius=10)
    button = ttk.Button(window, text="Open CSV", command=open_file)
    button.pack(side="top", pady=100)

    # 运行Tkinter窗口
    window.mainloop()
    # messagebox.showinfo("打开单位换算器", "打开单位换算器功能")


# 创建主窗口
window = tk.Tk()
window.title("功能选择")
# 设置窗口的宽度和高度
window_width = 400
window_height = 300

# 获取屏幕的宽度和高度
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# 计算窗口的初始位置
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# 设置窗口的位置和大小
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# 创建功能按钮
calculator_button = tk.Button(window, text="三维散点图", command=open_calculator)
unit_converter_button = tk.Button(window, text="二维折线图", command=open_unit_converter)

# 设置按钮的位置
calculator_button.pack(side="top", pady=50)
unit_converter_button.pack()

# 进入消息循环
window.mainloop()
