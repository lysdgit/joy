from pygattlib import GATTRequester

# 设置要保存的文件路径
received_file_path = 'received_file.txt'

# 定义用于接收数据的回调函数
def handle_data(handle, value):
    with open(received_file_path, 'wb') as file:
        file.write(value)
    print('文件接收完毕')
    print(f'文件保存在：{received_file_path}')
    requester.disconnect()  # 接收完文件后断开连接

# 初始化GATT请求器
requester = GATTRequester('B4:29:3D:6D:6C:C4', False)  # 替换为您的安卓设备的蓝牙地址

try:
    requester.connect(True)
    requester.read_by_uuid('00001101-0000-1000-8000-00805f9b34fb', callback=handle_data)  # 使用RFCOMM服务UUID

    print('等待文件接收...')
    input("按 Enter 键停止接收文件")
finally:
    requester.disconnect()
