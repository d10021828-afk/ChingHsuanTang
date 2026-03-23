import random
from flask import Flask, jsonify

app = Flask(__name__)

# 定義水晶資料庫
CRYSTALS = [
    {"name": "白水晶", "effect": "淨化磁場、提升專注力", "advice": "今日適合整理環境，清空雜念。"},
    {"name": "粉水晶", "effect": "增進人緣、守護愛情", "advice": "對身邊的人微笑，會有好運發生。"},
    {"name": "紫水晶", "effect": "開發智慧、穩定情緒", "advice": "冷靜思考後再做決定，直覺很準。"},
    {"name": "黃水晶", "effect": "招財進寶、充滿自信", "advice": "大膽展現你的才華，財運就在身邊。"},
    {"name": "黑曜石", "effect": "避邪擋煞、吸收負能量", "advice": "遠離負能量的人事物，守護好內心。"}
]

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>青玄堂｜水晶開運抽籤</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { 
                background: #121212; color: white; font-family: 'Microsoft JhengHei', sans-serif; 
                display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0;
            }
            .glass-card {
                background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(15px);
                border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px;
                padding: 40px; text-align: center; max-width: 600px; width: 90%;
            }
            .gold-text { color: #D4AF37; }
            #result-box {
                margin-top: 30px; padding: 20px; border-radius: 15px;
                background: rgba(212, 175, 55, 0.1); border: 1px dashed #D4AF37;
                display: none; /* 初始隱藏 */
            }
            .btn-draw {
                background: #D4AF37; color: black; font-weight: bold;
                border: none; padding: 15px 40px; border-radius: 50px; font-size: 1.2rem;
                transition: 0.3s; cursor: pointer;
            }
            .btn-draw:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(212, 175, 55, 0.5); }
        </style>
    </head>
    <body>
        <div class="glass-card">
            <h1 class="gold-text mb-4">🔮 今日水晶開運抽籤</h1>
            <p>靜下心來，點擊下方按鈕，領取你的今日能量指引。</p>
            
            <button class="btn-draw mt-4" onclick="drawCrystal()">即刻抽籤</button>

            <div id="result-box">
                <h2 id="crystal-name" class="gold-text"></h2>
                <p id="crystal-effect" class="fw-bold"></p>
                <hr style="border-color: rgba(255,255,255,0.2)">
                <p id="crystal-advice" class="small text-light"></p>
            </div>

            <div class="mt-5">
                <a href="/" style="color: #888; text-decoration: none; font-size: 0.8rem;">← 返回官網首頁</a>
            </div>
        </div>

        <script>
            function drawCrystal() {
                fetch('/draw')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result-box').style.display = 'block';
                        document.getElementById('crystal-name').innerText = data.name;
                        document.getElementById('crystal-effect').innerText = '✨ 能量：' + data.effect;
                        document.getElementById('crystal-advice').innerText = '💡 建議：' + data.advice;
                    });
            }
        </script>
    </body>
    </html>
    """

# 抽籤的後端 API 路徑
@app.route('/draw')
def draw():
    result = random.choice(CRYSTALS)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)