import serial
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM6', 115200,timeout=1)
x=[]

# 初始化图表
plt.ion()  # 打开交互模式
fig, ax = plt.subplots()
line, = ax.plot([], [])  # 创建空折线图

# 循环读取数据并更新图表
while True:
    # 十六进制数据
    hex_data = bytes.fromhex('FE F0 02 01 00 00 00 00') 
    ser.write(hex_data)
    # ser.write(b'SR,01,001\r\n')  # 发送指令，
    receive = ser.read(10) # 接收传感器响应
    hex_response = ' '.join(['{:02X}'.format(byte) for byte in receive])
    data_list = hex_response.split(" ")
    # print(data_list)

    # 获取右六位数据
    right_six = data_list[-3:]
    # print(right_six)

    zhengshu = int(right_six[0] , 16)
    zhengshu_str = str(zhengshu)

    xiaoshu = ''.join([str(right_six[1]), str(right_six[2])])
    xiaoshu = int(xiaoshu,16)
    xiaoshu_str = str(xiaoshu)
    now_data = zhengshu_str+"."+xiaoshu_str
    y = round(float(now_data),4)
    x = x+1
    print(x)
    print(y)
    
    # # 绘制曲线图
    # # plt.plot(  , color='blue', label='Temperature')
    # plt.plot(  y, color='black', label='Humidity')
    # plt.xlabel('Time')
    # plt.ylabel('Value')
    # plt.title('Temperature and Humidity Variation')
    # plt.legend()
    # plt.show()

    # 更新图表
    line.set_data(x,y)  # 设置新的数据
    # ax.relim()  # 重新计算轴界限
    # 设置轴界限的最小值和最大值
    ax.set_xlim(1, 20)
    ax.set_ylim(80, 100)
    ax.autoscale_view()  # 自动调整轴范围
    plt.draw()  # 绘制图表
    plt.pause(0.01)  # 暂停一小段时间，使图表能够更新



# 关闭串口连接
ser.close()