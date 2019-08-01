# -*- coding: utf-8 -*-

#HTTP 方法
# HTTP （与 Web 应用会话的协议）有许多不同的访问 URL 方法。默认情况下，
# 路由只回应 GET 请求，但是通过 route() 装饰器传递 methods 参数可以改变这个行为。

from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
      return 'POST'
    else:
      return 'GET'

if __name__ == '__main__':
    app.run(debug=True)