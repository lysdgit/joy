import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton
from PyQt5.QtSerialPort import QSerialPortInfo

class SerialPortWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Port Selector")
        self.setGeometry(100, 100, 300, 200)
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(50, 50, 200, 30)
        self.btn_select = QPushButton("Select", self)
        self.btn_select.setGeometry(100, 100, 100, 30)
        self.btn_select.clicked.connect(self.select_serial_port)
        serial_ports = QSerialPortInfo.availablePorts()
        for port in serial_ports:
            self.combo_box.addItem(port.portName())

    def select_serial_port(self):
        selected_port = self.combo_box.currentText()
        print("Selected Serial Port:", selected_port)
        self.close()
        
if __name__ == '__main__':
    app = QApplication([])
    window = SerialPortWindow()
    window.show()
    app.exec_()
    selected_port = window.combo_box.currentText()
    print("Selected Serial Port:", selected_port)
    subprocess.run(["python", "C:/Users/liys2/Desktop/pyRD/爱仕达/test3.py", selected_port])
