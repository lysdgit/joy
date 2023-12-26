import serial
import time
import datetime

def readdis(comx,bps,id,hz):
    # 创建串口对象
    com_port = "COM" + str(comx)
    # print(com_port)
    ser = serial.Serial(com_port, bps, timeout=0.1) 

    # 构建十六进制数据
    hex_data = bytes.fromhex(f'FE F0 {id:02X} 01 00 00 00 00')   
    # print(hex_data)
    ser.write(hex_data)

    # 读取串口返回的数据
    response = ser.read(10)  # 根据实际情况指定读取的字节数

    if response:
        # 将返回值转换为十六进制字符串，并打印出来
        hex_response = ' '.join(['{:02X}'.format(byte) for byte in response])
        # print('完整接收:', hex_response)
        # 拆分数据字符串
        data_list = hex_response.split(" ")
        # print('去空格接收:',data_list)


        # 获取右六位数据
        right_six = data_list[-3:]
        # print(right_six)

        zhengshu = int(right_six[0] , 16)
        zhengshu_str = str(zhengshu)

        xiaoshu = ''.join([str(right_six[1]), str(right_six[2])])
        xiaoshu = int(xiaoshu,16)
        xiaoshu_str = str(xiaoshu)

        now_data = zhengshu_str+"."+xiaoshu_str
        print(float(now_data))

        # 延时 
        time.sleep(hz)

        # 关闭串口
        ser.close()
    return now_data


readdis(6,115200,2,0.1)

