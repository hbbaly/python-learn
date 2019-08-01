# -*- coding: utf-8 -*-
# 模板渲染

# 用 Python 生成 HTML 十分无趣，而且相当繁琐，因为你必须手动对 HTML 做转义来保证应用的安全。为此，Flask 配备了 Jinja2 模板引擎。

# 你可以使用 render_template() 方法来渲染模板。你需要做的一切就是将模板名和你想作为关键字的参数传入模板的变量。这里有一个展示如何渲染模板的简例:

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)