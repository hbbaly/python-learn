# -*- coding: utf-8 -*-

# 路由系统

#  route() 装饰器把一个函数绑定到对应的 URL 上。
# 变量规则
from flask import Flask
app = Flask(__name__)

@app.route('/<int:id>/')
def hello_world(id):
    return 'Hello World!'+ str(id)


#  第一种情况中，指向 projects 的规范 URL 尾端有一个斜线。这种感觉很像在文件系统中的文件夹。访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范 URL 去。
@app.route('/projects/')
def projects():
    return 'The project page'


# 第二种情况的 URL 结尾不带斜线，类似 UNIX-like 系统下的文件的路径名。访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误。   
@app.route('/about')
def about():
    return 'The about page'
    
if __name__ == '__main__':
    app.run(debug=True)

# 可以把这些特殊的字段标记为 <variable_name> ， 
# 这个部分将会作为命名参数传递到你的函数。规则可以用 <converter:variable_name> 指定一个可选的转换器。

# int	接受整数
# float	同 int ，但是接受浮点数
# path	和默认的相似，但也接受斜线

