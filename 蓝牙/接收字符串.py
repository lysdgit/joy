# B4:29:3D:6D:6C:C4
import bluetooth
import time

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

# 这个UUID要与Android端使用的UUID相同
uuid = "00001101-0000-1000-8000-00805F9B34FB"

bluetooth.advertise_service(server_sock, "BluetoothServer", service_id=uuid, service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS])

while True:
    client_sock, client_info = server_sock.accept()
    print("已连接：", client_info)
    data = client_sock.recv(1024)
    result = data.decode().split("\n")
    print(result)
    print(result[2])
    print(result[3])
    client_sock.close()
    # 1秒延迟
    time.sleep(1)

server_sock.close()