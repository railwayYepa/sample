# app.py
import os
from flask import Flask, jsonify

app = Flask(__name__)

# 可通过环境变量自定义返回文本，默认 hello world
MESSAGE = os.getenv("MESSAGE", "hello world")
print("Message is:", os.getenv("MESSAGE", "hello world"))

@app.route("/")
def index():
    return MESSAGE

# 健康检查路由，方便 Railway 健检
@app.route("/healthz")
def healthz():
    return jsonify(ok=True)
