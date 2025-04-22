
from flask import Flask, jsonify, request

app = Flask(__name__)

# API route define karein
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, API working perfectly!"})

@app.route('/add', methods=['GET'])
def add():
    data = request.json
    result = data['num1'] + data['num2']
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)