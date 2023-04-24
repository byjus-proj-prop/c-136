from data import data
from flask import Flask, jsonify, request

app = Flask(__name__);

@app.route("/")
def home():
    return jsonify({"data": data, "msg": "success"}), 200;
@app.route("/planet")
def planet():
    name = request.args.get("name");
    planet_data = next(item for item in data if item["name"] == name);
    return jsonify({"data": planet_data, "msg": "success"}), 200;
if __name__ == "__main__":
    app.run();