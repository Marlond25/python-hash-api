from flask import Flask
from flask import request
from flask import make_response
from hashlib import sha256
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hash_api():
    return "Hello"

@app.route("/values", methods=["GET"])
def hash_ap():
    # file = open(r"db.txt", "w")
    # file.write(hashedValue)
    # file.close()
    return val

@app.route("/hash", methods=["POST"])
def hash():
    valueToHash = request.form.get("password")
    s = json.dumps(valueToHash, sort_keys = True)
    hashedValue = sha256(s.encode()).hexdigest()
    response = make_response({"password": hashedValue})
    response.headers["Content-Type"] = "application/json"
    # file = open(r"db.txt", "w")
    # file.write(hashedValue)
    # file.close()
    return response


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
