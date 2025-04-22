
from flask import Flask, jsonify

app = Flask(__name__)




@app.route('/', methods=['GET'])
def hello_world():
    return  "Hello, World!, amit, ajinkya, mohini, suveran,arun"


if __name__ == '__main__':
    app.run(debug=True)
