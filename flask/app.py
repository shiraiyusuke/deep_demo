# -*- coding: utf-8 -*-
# app.py
from flask import Flask
app = Flask(__name__)

# app.py
@app.route('/')
def index():
    # 「templates/index.html」のテンプレートを使う
    # 「message」という変数に"Hello"と代入した状態で、テンプレート内で使う
    return render_template('index.html', message="Hello")

if __name__ == "__main__":
    app.run()

