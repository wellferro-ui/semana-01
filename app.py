from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def inicio():
    return jsonify({"mensagem": "API de chamados em funcionamento"}), 200
