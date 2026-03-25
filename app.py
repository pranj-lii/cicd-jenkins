from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "CI/CD Pipeline Successful! The Flask App is Running."

if __name__ == '__main__':
    # Hosted on 0.0.0.0 to be accessible within network/containers
    app.run(host='0.0.0.0', port=5000)