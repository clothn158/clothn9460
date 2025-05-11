from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "TAK Flask Server Running!"

@app.route("/position", methods=["POST"])
def position():
    data = request.json
    print("位置資料：", data)
    return "OK", 200

@app.route("/marker", methods=["POST"])
def marker():
    data = request.json
    print("標記資料：", data)
    return "Received", 200
