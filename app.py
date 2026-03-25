from flask import Flask, jsonify, render_template # 這裡多加了 render_template
import random

app = Flask(__name__)

# 水晶資料庫
CRYSTALS = [
    {"name": "白水晶", "effect": "淨化磁場、提升專注力"},
    {"name": "粉水晶", "effect": "增進人緣、守護愛情"},
    {"name": "紫水晶", "effect": "開發智慧、穩定情緒"},
    {"name": "黃水晶", "effect": "招財進寶、充滿自信"},
    {"name": "黑曜石", "effect": "避邪擋煞、吸收負能量"}
]

# 路由 1：顯示首頁
@app.route('/')
def home():
    return render_template('index.html') # 改成回傳網頁檔案

# 路由 2：抽籤 API
@app.route('/draw')
def draw():
    return jsonify(random.choice(CRYSTALS))

if __name__ == '__main__':
    app.run(debug=True) 