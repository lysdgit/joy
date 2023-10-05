import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel
from PyQt5.QtGui import QFont
import pandas as pd
import numpy  as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("计算RP")
        self.setGeometry(100, 100, 400, 300)
        button = QPushButton("Open CSV", self)
        button.setGeometry(100, 80, 200, 50)
        button.clicked.connect(self.open_file)

        # 居中显示窗口
        screen_geometry = QApplication.desktop().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())

        #显示结果
        self.l_label = QLabel(self)
        self.l_label.setGeometry(140, 150, 200, 50)
        self.s3_label = QLabel(self)
        self.s3_label.setGeometry(140, 170, 200, 50)
        self.rp_label = QLabel(self)
        self.rp_label.setGeometry(140, 190, 200, 50)
        # 设置字体大小为 16
        font = QFont()
        font.setPointSize(16)
        self.l_label.setFont(font)
        self.s3_label.setFont(font)
        self.rp_label.setFont(font)
        

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            data = pd.read_csv(file_path, skiprows=1, usecols=[0, 1, 2])
            first = pd.read_csv(file_path, nrows=1)

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
        l_avg=round(np.mean(l),4)

        sl=np.sqrt((sum((l-l_avg)**2))/(len(l)-1))
        rd=round(3*sl,4)
        rp = round(l_avg+rd,4)

        print(first)
        print("l:   "+str(l_avg))
        print("RD:  "+str(rd))
        print("RP:  "+str(rp))

        self.l_label.setText("l :"+str(l_avg))
        self.s3_label.setText("3S:"+str(rd))
        self.rp_label.setText("RP:"+str(rp))
        

        # a=int(l_avg*10000) 
        # m=int(a/10)
        # n=a-10*m
        # if (n<5):
        #     a=10*m
        # if (n>4):
        #     a=10*(m+1)      

        # b=int(rd*10000)
        # mm=int(a/10)
        # nn=a-10*mm
        # if (nn<5):
        #     a=10*mm
        # if (nn>4):
        #     a=10*(mm+1)  

        # for i in range(int(a)):
        #     print("🔲",end ='')
        # for i in range(int(b)):
        #     print("⬛",end ='')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
