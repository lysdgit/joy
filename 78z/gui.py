import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=22)

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
