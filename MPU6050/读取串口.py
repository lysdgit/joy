# encoding=utf-8
import serial
if __name__ == '__main__':
  com = serial.Serial('COM10', 115200)
  # data = com.read(10)
  data=com.readline
  print(data)