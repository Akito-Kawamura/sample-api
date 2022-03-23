from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health():
    return jsonify({"health": "ok"})

@app.route("/user", methods=["GET"])
def user():
    f = open('json_mock/user.json', 'r')
    result = json.load(f)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
