from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 15位大天使專業對應資料庫 (7s Soul Lab 核心數據)
ARCHANGEL_CARDS = [
    {"name": "大天使 米迦勒 (Michael)", "theme": "勇氣、保護、生命目的", "crystal": "舒俱徠石", "message": "我是大天使米迦勒。我正用強大的保護光芒環繞你，為你切斷恐懼與負面的束縛。請勇敢邁向你的生命目的。"},
    {"name": "大天使 拉斐爾 (Raphael)", "theme": "身體與心靈的療癒、旅行平安", "crystal": "孔雀石", "message": "我是大天使拉斐爾。我將翡翠綠的療癒能量注入你的細胞與心靈。請信任我正與你同行。"},
    {"name": "大天使 加百列 (Gabriel)", "theme": "溝通、藝術、傳遞訊息", "crystal": "黃水晶", "message": "我是大天使加百列。現在是表達內心真理的時刻，你的創意與文字具有力量。"},
    {"name": "大天使 烏列爾 (Uriel)", "theme": "智慧、靈感、解決問題", "crystal": "琥珀", "message": "我是大天使烏列爾。我將智慧的光火點亮你的心靈，為你帶來解決難題的靈感。"},
    {"name": "大天使 夏彌爾 (Chamuel)", "theme": "尋找失物、內在平靜", "crystal": "綠色螢石", "message": "我是大天使夏彌爾。我能看見萬物之間的連結，我會協助你找到最合適的路。"},
    {"name": "大天使 亞列爾 (Ariel)", "theme": "豐盛、照顧動物", "crystal": "粉晶", "message": "我是大天使亞列爾。大自然充滿了支持你的豐盛能量。請多接觸土地，我會協助你顯化資源。"},
    {"name": "大天使 麥達昶 (Metatron)", "theme": "淨化脈輪、時間管理", "crystal": "西瓜碧璽", "message": "我是大天使麥達昶。我正為你淨化能量場。請專注於優先順序，我會協助你管理能量。"},
    {"name": "大天使 約菲爾 (Jofiel)", "theme": "美化思想、空間與生活", "crystal": "紅褐鐵礦", "message": "我是大天使約菲爾。美化你的思想，你的世界就會跟著美化。我會協助你清理混亂。"},
    {"name": "大天使 漢尼爾 (Haniel)", "theme": "月亮能量、直覺", "crystal": "月光石", "message": "我是大天使漢尼爾。請順應月亮的節奏，信任你的直覺。這段時間請溫柔地傾聽內在指引。"},
    {"name": "大天使 拉吉爾 (Raziel)", "theme": "靈性智慧、解讀夢境", "crystal": "透明石英", "message": "我是大天使拉吉爾。我為你開啟宇宙奧秘的大門，協助你憶起靈魂深處的智慧。"},
    {"name": "大天使 拉貴爾 (Raguel)", "theme": "關係和諧、公平正義", "crystal": "海藍寶", "message": "我是大天使拉貴爾。我是秩序與正義的維護者。我正協助你修復人際摩擦，實現公平。"},
    {"name": "大天使 聖德芬 (Sandalphon)", "theme": "音樂、祈願傳遞", "crystal": "綠松石", "message": "我是大天使聖德芬。你的每一句祈禱都已被溫柔地接納。請留意生活中的兆頭。"},
    {"name": "大天使 薩基爾 (Zadkiel)", "theme": "慈悲、寬恕、學習", "crystal": "紫水晶", "message": "我是大天使薩基爾。我協助你釋放過去的評判。在學習過程中，我會點亮你的智慧。"},
    {"name": "大天使 耶利米爾 (Jeremiel)", "theme": "回顧生命、情緒轉化", "crystal": "紫晶", "message": "我是大天使耶利米爾。現在是溫和檢視過往、校正未來的時刻。"},
    {"name": "大天使 艾瑟瑞爾 (Azrael)", "theme": "安慰、陪伴憂傷", "crystal": "黃色方解石", "message": "我是大天使艾瑟瑞爾。在變動時刻我溫柔陪伴你。請允許悲傷自然流動。"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():
    # 隨機抽取大天使神諭
    card = random.choice(ARCHANGEL_CARDS)
    return jsonify(card)

if __name__ == '__main__':
    # 部署環境關閉 Debug 模式以確保資安
    app.run(debug=False)