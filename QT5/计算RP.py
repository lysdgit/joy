import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.font_manager import FontProperties
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

# 设置中文字体
font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=22)

class sandian(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("重复定位精度")
        self.select_file()  

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "计算RP", "", "CSV Files (*.csv)", options=options)
        if fileName:
            try:
                #做数据来源
                df = pd.read_csv(fileName, skiprows=1, usecols=[0, 1, 2]) 
                # df = df[~(df == 0).all(axis=1)]
                x = df['x'].values
                y = df['y'].values
                z = df['z'].values
            except:
                return
        else:
            return



class MainMenu(QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.setFixedSize(400, 300)
        self.setWindowTitle("芜湖钊晟智能科技")
        layout = QHBoxLayout()
        self.yuntu = QPushButton("三维散点图")
        font = self.yuntu.font()
        font.setPointSize(22)
        self.yuntu.setFont(font)
        self.yuntu.clicked.connect(self.open_calendar_menu)
        layout.addWidget(self.yuntu)
        self.setLayout(layout)
        
        # 居中显示窗口
        screen_geometry = QApplication.desktop().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())

    def open_calendar_menu(self):
        self.hide()
        calendar_menu.show()
        sandian()

class CalendarMenu(QWidget):
    def __init__(self, parent=None):
        super(CalendarMenu, self).__init__(parent)
        self.setFixedSize(400, 180)
        self.setWindowTitle("三维散点图")
        layout = QVBoxLayout()
        self.back_button = QPushButton("返回")
        font = self.back_button.font()
        font.setPointSize(16)
        self.back_button.setFont(font)
        self.back_button.clicked.connect(self.back_to_main_menu)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def back_to_main_menu(self):
        self.hide()
        main_menu.show()

if __name__ == "__main__":
    app = QApplication([])
    main_menu = MainMenu()
    calendar_menu = CalendarMenu()
    app.exec_()
