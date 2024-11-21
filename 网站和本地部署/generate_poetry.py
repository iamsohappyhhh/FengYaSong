from flask import Flask, request, jsonify, render_template
import torch
import pickle as p
from utils import make_one_hot_vec_target, invert_dict
import os

app = Flask(__name__)

# 模型和字典路径配置
model_files = {
    "tangshi": ("model_tangshi.pt", "wordDic_tangshi"),
    "songci": ("model_songci.pt", "wordDic_songci"),
    "yuanqu": ("model_yuanqu.pt", "wordDic_yuanqu")
}

max_length = 100

# 加载模型和字典的函数
def load_model_and_dict(model_type):
    model_path, word_dict_path = model_files[model_type]
    model = torch.load(model_path, map_location=torch.device('cpu'))
    model.eval()
    with open(word_dict_path, 'rb') as rFile:
        word_to_ix = p.load(rFile)
    return model, word_to_ix

@app.route('/')
def home():
    return render_template('Page4.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    word = data.get('word')
    model_type = data.get('model', 'tangshi')  # 默认使用唐诗

    if model_type not in model_files:
        return jsonify({'error': '无效的模型选择'}), 400

    model, word_to_ix = load_model_and_dict(model_type)
    ix_to_word = invert_dict(word_to_ix)

    def sample(startWord='<START>'):
        input = make_one_hot_vec_target(startWord, word_to_ix)
        hidden = (torch.zeros(1, 1, model.hidden_dim), torch.zeros(1, 1, model.hidden_dim))
        output_name = startWord if startWord != "<START>" else ""

        for i in range(max_length):
            output, hidden = model(input, hidden)
            topv, topi = output.data.topk(1)
            topi = topi.item()
            w = ix_to_word[topi]
            if w == "<EOP>":
                break
            output_name += w
            input = make_one_hot_vec_target(w, word_to_ix)
        return output_name

    if word:
        poem = sample(word)
        return jsonify({'poem': poem})
    return jsonify({'error': '无效的输入'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
