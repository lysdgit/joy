import socket
import os
import bluetooth


HOST = ''
PORT = 8888  # 替换为您希望使用的端口号
BUFFER_SIZE = 1024
ANDROID_DEVICE_ADDRESS = 'B4:29:3D:6D:6C:C4'

def receive_file(file_path):
    # 创建一个RFCOMM BluetoothSocket
    server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    # 绑定本地蓝牙地址和端口
    server_socket.bind((HOST, PORT))

    # 监听连接请求
    server_socket.listen(1)

    print('等待Android客户端连接...')

    # 接受连接请求
    client_socket, client_address = server_socket.accept()
    print('已连接：', client_address)

    # 检查设备地址是否匹配
    if client_address[0] != ANDROID_DEVICE_ADDRESS:
        print('来自非指定设备的连接，拒绝接收文件。')
        client_socket.close()
        server_socket.close()
        return

    # 接收文件数据并写入文件
    with open(file_path, 'wb') as file:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            file.write(data)

    print('文件接收完毕')
    print(f'文件保存在：{os.path.abspath(file_path)}')

    # 关闭连接
    client_socket.close()
    server_socket.close()

# 设置要保存的文件路径
received_file_path = 'receive4d_file.txt'

# 开始监听并接收文件
receive_file(received_file_path)
