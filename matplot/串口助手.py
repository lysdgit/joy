# data = b'\x01\x10\x00\x90\x00\x02\x04\x00\x02\x01\xEA\xDB\x1C'  # 这里是示例数据，根据你的需求修改
# -*- coding: utf-8 -*-
# @Time : 2022/11/29 14:49
# @Author : Administrator
# @Email : dolphintt@qq.com
# @File : 串口调试助手.py
# @Project : sdudy1
import time

from tkinter.ttk import *
from tkinter import *
import datetime
import serial  # 导入模块
import serial.tools.list_ports
import threading
from tkinter import messagebox
from ttkbootstrap import Style



global UART          #全局型式保存串口句柄
global RX_THREAD     #全局型式保存串口接收函数
global gui           #全局型式保存GUI句柄

tx_cnt=0 #发送字符数统计
rx_cnt=0 #接收字符数统计


def ISHEX(data):        #判断输入字符串是否为十六进制
    if len(data)%2:
        return False
    for item in data:
        if item not in '0123456789ABCDEFabcdef': #循环判断数字和字符
            return False
    return True


def uart_open_close(fun,com,bund):  #串口打开关闭控制
    global UART
    global RX_THREAD

    if fun==1:#打开串口
        try:
           UART = serial.Serial(com, bund, timeout=0.2)  # 提取串口号和波特率并打开串口
           if UART.isOpen(): #判断是否打开成功
               lock = threading.Lock()
               RX_THREAD = UART_RX_TREAD('URX1',lock)  #开启数据接收进程
               RX_THREAD.setDaemon(True)               #开启守护进程 主进程结束后接收进程也关闭 会报警告 不知道咋回事
               RX_THREAD.start()
               RX_THREAD.resume()
               return True
        except:
            return False
        return False
    else:                   #关闭串口
        print("关闭串口")
        RX_THREAD.pause()
        UART.close()

def uart_tx(data,isHex=False):          #串口发送数据
    global UART

    try:
        if  UART.isOpen():  #发送前判断串口状态 避免错误
            print("uart_send=" + data)
            gui.tx_rx_cnt(tx=len(data)) #发送计数
            if isHex:   #十六进制发送
                data_bytes = bytes.fromhex(data)
                return UART.write(bytes(data_bytes))
            else:      #字符发送
                return UART.write(data.encode('gb2312'))
    except:#错误返回
        messagebox.showinfo('错误', '发送失败')


class UART_RX_TREAD(threading.Thread):          #数据接收进程 部分重构
    global gui

    def __init__(self, name, lock):
        threading.Thread.__init__(self)
        self.mName = name
        self.mLock = lock
        self.mEvent = threading.Event()

    def run(self): #主函数
        print('开启数据接收\r')
        while True:
            self.mEvent.wait()
            self.mLock.acquire()
            if UART.isOpen():
                rx_buf =  UART.read()
                if len(rx_buf) >0:
                    rx_buf += UART.readall()  #有延迟但不易出错
                    gui.tx_rx_cnt(rx=len(rx_buf))
                    if gui.ascii_hex_get() == False:
                        print('收到hex数据', rx_buf.hex().upper())
                        gui.txt_rx.insert(END,  rx_buf.hex().upper())
                    else:
                        str_data = str(rx_buf, encoding='gb2312')
                        print("串口收到消息:", len(rx_buf), str_data)
                        gui.txt_rx.insert(END,str_data)
                        # self.txt_rx.insert(END,str_data)
            self.mLock.release()
           #time.sleep(3)
    def pause(self): #暂停
        self.mEvent.clear()

    def resume(self):#恢复
        self.mEvent.set()


'''GUI'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('梵德觅串口调试助手')             #窗口名称
        self.root.geometry("800x360+500+150")         #尺寸位置
        self.interface()
        Style(theme='pulse') #主题修改 可选['cyborg', 'journal', 'darkly', 'flatly' 'solar', 'minty', 'litera', 'united', 'pulse', 'cosmo', 'lumen', 'yeti', 'superhero','sandstone']


    def interface(self):
        """"界面编写位置"""
        #--------------------------------操作区域-----------------------------#
        self.fr1=Frame(self.root)
        self.fr1.place(x=0,y=0,width=180,height=360)     #区域1位置尺寸

        self.lb1 =Label(self.fr1, text='端口号：',font="微软雅黑",fg='red')  #点击可刷新
        self.lb1.place(x=0,y=5,width=100,height=35)

        self.var_cb1 = StringVar()
        self.comb1 = Combobox(self.fr1,textvariable=self.var_cb1)
        self.comb1['values'] = list(serial.tools.list_ports.comports()) #列出可用串口
        self.comb1.current(0)  # 设置默认选项 0开始
        self.comb1.place(x=10,y=40,width=150,height=30)
        com=list(serial.tools.list_ports.comports())

        print('**********可用串口***********')
        for i in range(0, len(com)):
            print(com[i])
        print('***************************')

        self.lb2 = Label(self.fr1, text='波特率：')
        self.comb2 = Combobox(self.fr1,values=['2400','9600','57600','115200'])
        self.comb2.current(3)                               #设置默认选项 115200
        self.lb2.place(x=5,y=75,width=60,height=20)
        self.comb2.place(x=10,y=100,width=100,height=25)

        self.var_bt1 = StringVar()
        self.var_bt1.set("打开串口")
        self.btn1 = Button(self.fr1,textvariable=self.var_bt1,command=self.uart_opn_close) #绑定 uart_opn_close 方法
        self.btn1.place(x=10,y=140,width=60,height=30)



        self.var_cs = IntVar()  #定义返回类型
        self.rd1 = Radiobutton(self.fr1,text="Ascii",variable=self.var_cs,value=0,command = self.txt_clr) #选择后清除显示内容
        self.rd2 = Radiobutton(self.fr1,text="Hex",variable=self.var_cs,value=1,command = self.txt_clr)
        self.rd1.place(x=5,y=180,width=60,height=30)
        self.rd2.place(x=5,y=210,width=60,height=30)


        self.btn3 = Button(self.fr1, text='清空',command = self.txt_clr) #绑定清空方法
        self.btn4 = Button(self.fr1, text='保存',command=self.savefiles) #绑定保存方法
        self.btn3.place(x=10,y=260,width=60,height=30)
        self.btn4.place(x=100,y=260,width=60,height=30)

        self.btn5 = Button(self.fr1, text='功能',command=self.ascii_hex_get) #测试用
        self.btn6 = Button(self.fr1, text='发送',command=self.uart_send)  #绑定发送方法
        self.btn5.place(x=10,y=315,width=60,height=30)
        self.btn6.place(x=100,y=315,width=60,height=30)

        #-------------------------------文本区域-----------------------------#
        self.fr2=Frame(self.root)          #区域1 容器  relief   groove=凹  ridge=凸
        self.fr2.place(x=180,y=0,width=620,height=360)     #区域1位置尺寸

        self.txt_rx = Text(self.fr2)
        self.txt_rx.place(relheight=0.6,relwidth=0.9,relx=0.05,rely=0.01) #比例计算控件尺寸和位置

        self.txt_tx = Text(self.fr2)
        self.txt_tx.place(relheight=0.25,relwidth=0.9,relx=0.05,rely=0.66) #比例计算控件尺寸位置

        self.lb3 =Label(self.fr2, text='接收:0    发送:0',bg="yellow",anchor='w') #字节统计
        self.lb3.place(relheight=0.05,relwidth=0.3,relx=0.045,rely=0.925)

        self.lb4 = Label(self.fr2, text=' ', anchor='w',relief=GROOVE)  #时钟
        self.lb4.place(relheight=0.05, relwidth=0.1, relx=0.85, rely=0.935)
#------------------------------------------方法-----------------------------------------------
    def gettim(self):#获取时间 未用
            timestr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
            self.lb4.configure(text=timestr)  # 重新设置标签文本
            # tim_str = str(datetime.datetime.now()) + '\n'
            # self.lb4['text'] = tim_str
            self.txt_rx.after(1000, self.gettim)     # 每隔1s调用函数 gettime 自身获取时间 GUI自带的定时函数

    def txt_clr(self):#清空显示
        self.txt_rx.delete(0.0, 'end')  # 清空文本框
        self.txt_tx.delete(0.0, 'end')  # 清空文本框

    def ascii_hex_get(self):#获取单选框状态
        if(self.var_cs.get()):
            return False
        else:
            return True

    def uart_opn_close(self):#打开关闭串口
        if(self.var_bt1.get() == '打开串口'):
          if(uart_open_close(1,str(self.comb1.get())[0:5],self.comb2.get())==True): #传递下拉框选择的参数 COM号+波特率  【0:5】表示只提取COM号字符
             self.var_bt1.set('关闭串口')                             #改变按键内容
             self.txt_rx.insert(0.0, self.comb1.get() + ' 打开成功\r\n')  # 开头插入
          else:
             print("串口打开失败")
             messagebox.showinfo('错误','串口打开失败')
        else:
            uart_open_close(0, 'COM1', 115200) #关闭时参数无效
            self.var_bt1.set('打开串口')

    def uart_send(self): #发送数据
        send_data = self.txt_tx.get(0.0, 'end').strip()
        if self.ascii_hex_get():    #字符发送
            uart_tx(send_data)
        else:
            send_data = send_data.replace(" ", "").replace("\n", "0A").replace("\r", "0D") #替换空格和回车换行
            if(ISHEX(send_data)==False):
                messagebox.showinfo('错误', '请输入十六进制数')
                return
            uart_tx(send_data,True)

    def tx_rx_cnt(self,rx=0,tx=0):  #发送接收统计
        global tx_cnt
        global rx_cnt

        rx_cnt += rx
        tx_cnt += tx
        self.lb3['text'] = '接收：'+str(rx_cnt),'发送：'+str(tx_cnt)

    def savefiles(self):   #保存日志TXT文本
        try:
            with open('log.txt','a') as file:       #a方式打开 文本追加模式
                file.write(self.txt_rx.get(0.0,'end'))
                messagebox.showinfo('提示', '保存成功')
        except:
            messagebox.showinfo('错误', '保存日志文件失败！')


if __name__ == '__main__':
    print('Star...')
    gui = GUI()
    gui.gettim()  #开启时钟
    gui.root.mainloop()
    UART.close()   #结束关闭 避免下次打开错误
    print('End...')

