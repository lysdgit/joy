def calculate_crc16_modbus(data):
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc


character = 'A'

# 获取字符的 ASCII 值
ascii_value = ord(character)

# 将 ASCII 值转换为十六进制表示
hex_value = hex(ascii_value)
hex_number = hex(hex_value)

# 示例数据
data1 = [0x01, 0x10, 0x00, 0x70, 0x00, 0x06, 0x0C]
data2 = [hex_number]
data3 = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
data=data1+data2+data3

print(data)
# 计算 CRC16 Modbus
crc = calculate_crc16_modbus(data)

# 输出结果
print(f"CRC16 Modbus: 0x{crc:04X}")

def reverse_hex_string(hex_string):
    reversed_string = ""
    for i in range(0, len(hex_string), 2):
        reversed_string = hex_string[i:i+2] + reversed_string
    return reversed_string

# 将 CRC16 Modbus 转换为逆向的十六进制字符串表示
hex_string = f"{crc:04X}"
reversed_hex_string = reverse_hex_string(hex_string)

# 输出结果
print("Reversed CRC16 Modbus: 0x" + reversed_hex_string)
