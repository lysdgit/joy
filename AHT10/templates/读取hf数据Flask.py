from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Function to get data from the database
def get_data():
    connection = mysql.connector.connect(
        host='mysql.sqlpub.com',
        user='userlys',
        password='b7b573ab3e2a2ed0',
        database='lysupload'
    )
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM wendu")
    cursor.execute("SELECT * FROM wendu ORDER BY id DESC LIMIT 20") 
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

@app.route("/")
def index():
    # Fetch data when a request is made
    rows = get_data()
    return render_template("hf.html", rows=rows)

if __name__ == "__main__":
    app.run(port=2096)


