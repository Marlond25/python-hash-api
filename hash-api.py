from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hash_api():
    return "Hello"

@app.route('/hash', methods=['POST'])
def hash():
    return request.args.get('username', '')


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
