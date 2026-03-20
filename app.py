import time
from flask import Flask
import mysql.connector

app = Flask(__name__)

# Retry connection until MySQL is ready
for i in range(10):
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="testdb"
        )
        print("✅ Connected to MySQL")
        break
    except:
        print("⏳ Waiting for MySQL...")
        time.sleep(3)

@app.route('/')
def home():
    return "Flask + MySQL is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)