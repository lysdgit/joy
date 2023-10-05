import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import pandas as pd
import matplotlib.pyplot as plt


  
def open_file_dialog():
    file_path, _ = QFileDialog.getOpenFileName("Open CSV", "", "CSV Files (*.csv)")
    if file_path:
        data = pd.read_csv(file_path)
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

open_file_dialog
