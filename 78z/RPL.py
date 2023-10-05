import pandas as pd
import numpy as np
# 读取数据
data = pd.read_csv(r'D:\Project\RRT\LDS-E测试\907\97.csv', skiprows=1, usecols=[0, 1, 2])
x = data['x'].values
y = data['y'].values
z = data['z'].values

x_avg = np.mean(x) #x的均值
y_avg = np.mean(y) #y的均值
z_avg = np.mean(z) #z的均值

delta_x = np.abs(x-x_avg)
delta_y = np.abs(y-y_avg)
delta_z = np.abs(z-z_avg)

l=np.sqrt((delta_x**2)+(delta_y**2)+(delta_z**2))
l_avg=np.mean(l)

sl=np.sqrt((sum((l-l_avg)**2))/(len(l)-1))
rd=3*sl
rp = l_avg+rd


print("l:   "+str(l_avg))
print("RD:  "+str(rd))
print("RP:  "+str(rp))


# print("l/RD")
# print(l_avg/rd)

def sishewuru(a):
    m=int(a/10)
    n=a-10*m
    if (n<5):
        a=10*m
    if (n>4):
        a=10*(m+1)
    return a

a=int(l_avg*10000)    
b=int(rd*10000)

a = float(sishewuru(a))/10
b = float(sishewuru(b))/10

for i in range(int(a)):
    print("🔲",end ='')
for i in range(int(b)):
    print("⬛",end ='')

