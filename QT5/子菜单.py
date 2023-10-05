import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt5.QtCore import Qt

# 自定义菜单界面类1
class MenuPage1(QWidget):
    def __init__(self, parent=None):
        super(MenuPage1, self).__init__(parent)
        label = QLabel("菜单界面1", self)
        label.setAlignment(Qt.AlignCenter)

# 自定义菜单界面类2
class MenuPage2(QWidget):
    def __init__(self, parent=None):
        super(MenuPage2, self).__init__(parent)
        label = QLabel("菜单界面2", self)
        label.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建主界面窗口
    mainWindow = QWidget()
    layout = QVBoxLayout(mainWindow)

    # 创建菜单界面切换按钮
    btnMenu1 = QPushButton("菜单1")
    btnMenu2 = QPushButton("菜单2")

    # 创建菜单界面堆栈
    stackedWidget = QStackedWidget()

    # 创建菜单界面
    menuPage1 = MenuPage1()
    menuPage2 = MenuPage2()

    # 将菜单界面添加到堆栈
    stackedWidget.addWidget(menuPage1)
    stackedWidget.addWidget(menuPage2)

    # 设置默认显示的菜单界面
    stackedWidget.setCurrentWidget(menuPage1)

    # 连接按钮的点击信号和切换菜单界面的槽函数
    btnMenu1.clicked.connect(lambda: stackedWidget.setCurrentWidget(menuPage1))
    btnMenu2.clicked.connect(lambda: stackedWidget.setCurrentWidget(menuPage2))

    # 将按钮和菜单界面堆栈添加到主界面布局中
    layout.addWidget(btnMenu1)
    layout.addWidget(btnMenu2)
    layout.addWidget(stackedWidget)

    # 显示主界面窗口
    mainWindow.show()

    sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedWidget, QLabel


# class Menu1(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("This is Menu 1"))
#         self.setLayout(layout)


# class Menu2(QWidget):
#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("This is Menu 2"))
#         self.setLayout(layout)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # 创建主要的显示区域
#         self.stacked_widget = QStackedWidget()
#         self.setCentralWidget(self.stacked_widget)

#         # 创建菜单界面
#         self.menu1 = Menu1()
#         self.menu2 = Menu2()

#         # 将菜单界面添加到QStackedWidget
#         self.stacked_widget.addWidget(self.menu1)
#         self.stacked_widget.addWidget(self.menu2)

#         # 创建菜单按钮
#         self.button1 = QPushButton("Menu 1")
#         self.button2 = QPushButton("Menu 2")

#         # 连接按钮的点击事件到切换界面的槽函数
#         self.button1.clicked.connect(self.switch_to_menu1)
#         self.button2.clicked.connect(self.switch_to_menu2)

#         # 创建一个垂直布局，并添加菜单按钮
#         layout = QVBoxLayout()
#         layout.addWidget(self.button1)
#         layout.addWidget(self.button2)

#         # 创建一个容器的QWidget，并将布局设置为QWidget的布局
#         container = QWidget()
#         container.setLayout(layout)

#         # 将容器的QWidget添加到主窗口的状态栏
#         self.statusBar().addWidget(container)

#     def switch_to_menu1(self):
#         self.stacked_widget.setCurrentWidget(self.menu1)

#     def switch_to_menu2(self):
#         self.stacked_widget.setCurrentWidget(self.menu2)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
