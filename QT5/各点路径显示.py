import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=22)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("路径折线图")
        self.setGeometry(100, 100, 400, 300)
        button = QPushButton("Open CSV", self)
        button.setGeometry(100, 100, 200, 50)
        button.clicked.connect(self.open_file)

        # 居中显示窗口
        screen_geometry = QApplication.desktop().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            data = pd.read_csv(file_path, skiprows=1, usecols=[0, 1, 2])

            x = data['x'].values
            y = data['y'].values
            z = data['z'].values

            x_avg = np.mean(x) #x的均值
            y_avg = np.mean(y) #y的均值
            z_avg = np.mean(z) #z的均值

            delta_x = np.abs(x-x_avg)
            delta_y = np.abs(y-y_avg)
            delta_z = np.abs(z-z_avg)

            l=np.sqrt((delta_x**2)+(delta_y**2)+(delta_z**2))
            l_avg=np.mean(l)

            sl=np.sqrt((sum((l-l_avg)**2))/(len(l)-1))
            rd=3*sl
            rp = l_avg+rd
            rp = "{:.4f}".format(rp)
            rp = "R:" +rp

            # 创建3D图形对象
            fig = plt.figure(figsize=(13, 6))
            ax = fig.add_subplot(111, projection='3d')

            # 绘制散点图和路径
            for i in range(len(x)):
                ax.scatter(x[i], y[i], z[i], c='r', marker='o')
                ax.text(x[i], y[i], z[i], str(i+1), color='black', fontsize=12)
            if len(x) > 1:
                ax.plot(x, y, z, c='b')

            # 设置坐标轴标签
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')

            # 显示图形
            plt.title(rp, fontproperties=font)
            plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
