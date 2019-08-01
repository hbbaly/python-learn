from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()


# 如果你禁用了 debug 或信任你所在网络的用户，你可以简单修改调用 run() 的方法使你的服务器公开可用，如下:

# app.run(host='0.0.0.0')
# 这会让操作系统监听所有公网 IP。