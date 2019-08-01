
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

# 调试模式 绝对不能用于生产环境 。

# 虽然 run() 方法适用于启动本地的开发服务器，但是你每次修改代码后都要手动重启它。
# 1.
# app.debug = True
# app.run()

#2.
# app.run(debug=True)