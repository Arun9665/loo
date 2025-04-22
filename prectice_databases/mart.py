
from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {'id':1,'tital':'book'},
    {'id':1,'tital':'book'},
    {'id':1,'tital':'book'},
    {'id':1,'tital':'book'},
    {'id':1,'tital':'book'}


]


@app.route('/', methods=['GET'])
def hello_world():
    return  "Hello, World!"

@app.route('/books', methods=['GET'])
def get_world():
    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)
