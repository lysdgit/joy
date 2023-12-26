from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# 连接到MySQL数据库
connection = mysql.connector.connect(
        host='mysql.sqlpub.com',
        user='lysdsql',
        password='46771b53bb625790',
        database='lystest'
)

# 创建游标对象
cursor = connection.cursor()

# 执行查询
cursor.execute("SELECT * FROM aht10")
rows = cursor.fetchall()
# print(rows)

# 关闭游标和数据库连接
cursor.close()
connection.close()

@app.route("/")
def index():
    # return "Hello, world!"
    return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run()
