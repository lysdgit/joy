import mysql.connector
import matplotlib.pyplot as plt
# 连接到MySQL数据库
cnx = mysql.connector.connect(
    host='mysql.sqlpub.com',
    user='lysdsql',
    password='46771b53bb625790',
    database='lystest'
)

# 创建游标对象
cursor = cnx.cursor()

# 执行查询语句
query = "SELECT temperature, humidity FROM aht10"
cursor.execute(query)

# 从查询结果中提取温度和湿度数据，并存储在对应的列表中
temperature_data = []
humidity_data = []


for row in cursor.fetchall():
    temperature_data.append(row[0])
    humidity_data.append(row[1])

# 关闭游标和数据库连接
cursor.close()
cnx.close()

# 打印温度和湿度数据列表
# print("Temperature Data:", temperature_data)
# print("Humidity Data:", humidity_data)


# 绘制温度和湿度曲线图
plt.plot(  temperature_data, color='blue', label='Temperature')
plt.plot(  humidity_data, color='black', label='Humidity')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Temperature and Humidity Variation')
plt.legend()
plt.show()
# # 绘制温度曲线图
# plt.plot( temperature_data, label='Temperature')
# plt.xlabel('Time')
# plt.ylabel('Temperature (°C)')
# plt.title('Temperature Variation')
# plt.legend()
# plt.show()

# # 绘制湿度曲线图
# plt.plot( humidity_data, label='Humidity')
# plt.xlabel('Time')
# plt.ylabel('Humidity (%)')
# plt.title('Humidity Variation')
# plt.legend()
# plt.show()