# -*- coding: utf-8 -*-

# 构造 URL
#  url_for() 来给指定的函数构造 URL。它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。未知变量部分会添加到 URL 末尾作为查询参数。

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():pass

@app.route('/login')
def login (): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
  print(url_for('index'))
  print(url_for('login'))
  print(url_for('login', name='hbb'))
  print(url_for('profile', username ='hbbaly'))
  
#  /
# /login
# /login?name=hbb
# /user/hbbaly

if __name__ == '__main__':
    app.run(debug=True)
