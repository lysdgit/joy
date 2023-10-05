import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from tkinter import ttk
def zhexian():
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

zhexian()
