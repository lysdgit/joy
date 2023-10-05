import bluetooth

# 设置蓝牙参数
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1  # RFCOMM通道1是默认的蓝牙串行通信端口
server_socket.bind(("", port))
server_socket.listen(1)

# 等待客户端连接
print("等待安卓客户端连接...")
client_socket, client_address = server_socket.accept()
print("已连接到安卓客户端：", client_address)

# 接收数据
data = client_socket.recv(1024)
received_text = data.decode("utf-8")  # 假设txt文本是以utf-8编码发送的
print("接收到的文本：", received_text)

# 关闭连接
client_socket.close()
server_socket.close()
