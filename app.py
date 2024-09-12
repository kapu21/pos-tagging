from flask import Flask, request, render_template, jsonify
import spacy

# Flaskアプリの初期化
app = Flask(__name__)

# Spacyモデルのロード
nlp = spacy.load('en_core_web_sm')

# 品詞解析APIのエンドポイント
@app.route('/parse', methods=['POST'])
def parse_text():
    data = request.json
    text = data.get('text', '')
    doc = nlp(text)
    
    result = []
    for token in doc:
        result.append({
            'text': token.text,
            'pos': token.pos_,
            'color': get_color_for_pos(token.pos_)
        })
    
    return jsonify(result)

# 品詞に対応する色を指定
def get_color_for_pos(pos):
    colors = {
        "NOUN": "#1E90FF",
        "VERB": "#32CD32",
        "ADJ": "#FF69B4",
        "ADV": "#FFA500",
        "PRON": "#9370DB",
        "DET": "#00CED1",
        "CONJ": "#D2691E",
        "INTJ": "#FF4500",
        "AUX": "#FFD700",
        "NUM": "#8B4513",
        "PREP": "#A9A9A9",
        "SCONJ": "#8A2BE2",
        "PART": "#B8860B",
        "SYM": "#FF6347",
        "X": "#FF00FF"
    }
    return colors.get(pos, "#000000")  # 該当しない場合は黒

# フロントエンドページのルーティング
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
