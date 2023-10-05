from PyQt5.QtCore import QObject, pyqtSignal

class ClassA(QObject):
    jump_signal = pyqtSignal(str)  # 定义一个字符串类型的信号

    def jump(self):
        self.jump_signal.emit("跳转到ClassB")  # 发射信号

class ClassB(QObject):
    def __init__(self):
        super().__init__()

    def jump_to_class_b(self, message):
        print("接收到信号，跳转到ClassB")

if __name__ == '__main__':
    class_a = ClassA()
    class_b = ClassB()

    class_a.jump_signal.connect(class_b.jump_to_class_b)  # 连接信号和槽

    class_a.jump()  # 触发跳转操作
