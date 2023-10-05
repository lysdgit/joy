import pandas as pd

if __name__ == '__main__':
   mat=pd.read_csv("C:/Users/liys2/Desktop/pyRD/MPU6050/22.txt",header=None,delimiter=",")
df=pd.DataFrame(mat)
df.to_csv("C:/Users/liys2/Desktop/pyRD/MPU6050/22.csv")