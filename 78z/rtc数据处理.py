import pandas as pd
import datetime

# 读取 CSV 文件为 pandas.DataFrame 对象
df = pd.read_csv('C:/Users/liys2/Desktop/1.csv', skiprows=2)

# 将前两行读取到另一个DataFrame中
header = pd.read_csv('C:/Users/liys2/Desktop/1.csv', nrows=2, header=None)

# 将每一行减去第一行
df = df.apply(lambda x: x - df.iloc[0], axis=1).round(3)


# 合并处理后的数据和原始数据
df = pd.concat([df,header], ignore_index=True)


# 获取当前时间作为文件名的一部分
now = datetime.datetime.now().strftime('%m-%d-%Y-_%H-%M-%S')

# 将结果保存为 txt 文件，文件名以当前时间命名
df.to_csv(f'RTC_{now}.txt', sep='\t', index=False)
