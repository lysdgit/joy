import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("主界面")
        
        button1 = tk.Button(self, text="跳转到界面1", command=self.show_page1)
        button1.pack()
        
        button2 = tk.Button(self, text="跳转到界面2", command=self.show_page2)
        button2.pack()
        
    def show_page1(self):
        self.withdraw()  # 隐藏主界面
        page1 = Page1(self)  # 创建界面1实例
        page1.mainloop()
        self.deiconify()  # 显示主界面
        
    def show_page2(self):
        self.withdraw()  # 隐藏主界面
        page2 = Page2(self)  # 创建界面2实例
        page2.mainloop()
        self.deiconify()  # 显示主界面

class Page1(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("界面1")
        
        button = tk.Button(self, text="返回主界面", command=self.close)
        button.pack()
        
    def close(self):
        self.destroy()  # 关闭界面1

class Page2(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.title("界面2")
        
        button = tk.Button(self, text="返回主界面", command=self.close)
        button.pack()
        
    def close(self):
        self.destroy()  # 关闭界面2

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
