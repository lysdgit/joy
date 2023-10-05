import tkinter as tk

def button_click(num):
    current = result.get()
    result.set(current + num)

def button_clear():
    result.set("")

def button_equal():
    current = result.get()
    try:
        result.set(eval(current))
    except:
        result.set("Error")

# 创建主窗口
caculate = tk.Tk()
caculate.title("计算器")

# 创建显示结果的文本框
result = tk.StringVar()
result.set("")
display = tk.Entry(caculate, textvariable=result, width=20)
display.grid(row=0, column=0, columnspan=4)

# 创建按钮并绑定功能
button_1 = tk.Button(caculate, text="1", command=lambda: button_click("1"))
button_1.grid(row=1, column=0)
button_2 = tk.Button(caculate, text="2", command=lambda: button_click("2"))
button_2.grid(row=1, column=1)
button_3 = tk.Button(caculate, text="3", command=lambda: button_click("3"))
button_3.grid(row=1, column=2)
button_add = tk.Button(caculate, text="+", command=lambda: button_click("+"))
button_add.grid(row=1, column=3)
button_4 = tk.Button(caculate, text="4", command=lambda: button_click("4"))
button_4.grid(row=2, column=0)
button_5 = tk.Button(caculate, text="5", command=lambda: button_click("5"))
button_5.grid(row=2, column=1)
button_6 = tk.Button(caculate, text="6", command=lambda: button_click("6"))
button_6.grid(row=2, column=2)
button_subtract = tk.Button(caculate, text="-", command=lambda: button_click("-"))
button_subtract.grid(row=2, column=3)
button_7 = tk.Button(caculate, text="7", command=lambda: button_click("7"))
button_7.grid(row=3, column=0)
button_8 = tk.Button(caculate, text="8", command=lambda: button_click("8"))
button_8.grid(row=3, column=1)
button_9 = tk.Button(caculate, text="9", command=lambda: button_click("9"))
button_9.grid(row=3, column=2)
button_multiply = tk.Button(caculate, text="*", command=lambda: button_click("*"))
button_multiply.grid(row=3, column=3)
button_clear = tk.Button(caculate, text="C", command=button_clear)
button_clear.grid(row=4, column=0)
button_0 = tk.Button(caculate, text="0", command=lambda: button_click("0"))
button_0.grid(row=4, column=1)
button_equal = tk.Button(caculate, text="=", command=button_equal)
button_equal.grid(row=4, column=2)
button_divide = tk.Button(caculate, text="/", command=lambda: button_click("/"))
button_divide.grid(row=4, column=3)

# 进入消息循环
caculate.mainloop()
