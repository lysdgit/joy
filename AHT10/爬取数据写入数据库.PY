import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
import time

def timer(n):
 while True:
    print(time.strftime('%Y-%m-%d %X',time.localtime()))
    print("开始执行任务")  # 此处为要执行的任务

    # 获取当前时间
    current_time = datetime.now()  

    # 获取HTML页面内容
    url = "http://192.168.1.120"  # 替换为实际的HTML页面URL
    response = requests.get(url)
    html_content = response.text

    # 解析HTML页面数据
    soup = BeautifulSoup(html_content, 'html.parser')
    h2_tag = soup.find('h2')
    temperature_value = h2_tag.text.strip()  # 获取<h2>标签的文本内容，并去除首尾的空白字符
    # print(temperature_value)

    h3_tag = soup.find('h3')
    humidity_value = h3_tag.text.strip()  # 获取<h3>标签的文本内容，并去除首尾的空白字符
    # print(humidity_value)

    # 连接MySQL数据库
    cnx = mysql.connector.connect(
        host='mysql.sqlpub.com',
        user='lysdsql',
        password='46771b53bb625790',
        database='lystest'
    )
    cursor = cnx.cursor()

    # 插入温度数据到MySQL数据库
    insert_query = "INSERT INTO aht10 (temperature, humidity, timestamp) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (temperature_value, humidity_value, current_time))
    cnx.commit()

    # 关闭数据库连接
    cursor.close()
    cnx.close()

    time.sleep(n)

#10秒执行一次
timer(60)

#测试是否阻塞
print("测试是否阻塞")