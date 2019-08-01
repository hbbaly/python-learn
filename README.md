# python操作MySql

## mysql基础知识

[mysql基础知识](https://hbbaly.github.io/database/mysql.html#%E5%AE%89%E8%A3%85%EF%BC%9A)

## python链接数据库

安装`PyMySQL`

```js
pip3 install PyMySQL
```
```py
import pymysql

# 打开数据库连接  ip 用户名 密码 数据库
db = pymysql.connect("localhost","root","123456789","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
db.close()
```

## 创建数据表

```py
# 创建数据库 EMPLOYEE
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","123456789","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
 
cursor.execute(sql)
 
# 关闭数据库连接
db.close()
```

### 插入数据

```py
#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","123456789","test" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()
```

## 查询一条数据

```py
# 使用pymysql链接mysql
import pymysql

# 打开数据库连接  ip 用户名 密码 数据库
db = pymysql.connect("localhost","root","123456789","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL
cursor.execute("""SELECT * FROM `EMPLOYEE`""")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print (data)
 
# 关闭数据库连接
db.close()
```
## 查询所有

```py
# fetchall查询所有
# 使用pymysql链接mysql
import pymysql

# 打开数据库连接  ip 用户名 密码 数据库
db = pymysql.connect("localhost","root","123456789","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
cursor.execute("""SELECT * FROM `EMPLOYEE`""")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
 
print (data)
 
# 关闭数据库连接
db.close()
```

## 更新数据

```py
# 使用pymysql链接mysql
import pymysql

# 打开数据库连接  ip 用户名 密码 数据库
db = pymysql.connect("localhost","root","123456789","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = """UPDATE `EMPLOYEE` SET AGE = AGE + 18"""
try:
  cursor.execute(sql)
  db.commit()
except:
  db.rollback()
 
# 关闭数据库连接
db.close()
```
## 删除数据

```py
# 使用pymysql链接mysql
import pymysql

# 打开数据库连接  ip 用户名 密码 数据库
db = pymysql.connect("localhost","root","123456789","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = """DELETE FROM `EMPLOYEE` WHERE AGE > 30"""
try:
  cursor.execute(sql)
  db.commit()
except:
  db.rollback()
 
# 关闭数据库连接
db.close()
```

## ORM 使用

```py
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'news'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


engine = create_engine('mysql+pymysql://root:123456789@localhost:3306/test')
# 创建表
Base.metadata.create_all(engine)

# 插入数据
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 插入数据
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='2', name='ly')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 查询及更新
# 创建session对象:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print ('name:', user.name)
# 更新
user.name = 'hbbaly1314'
print ('name:', user.name)

session.commit()
# 关闭Session:
session.close()

# 删除数据
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()

# 删除
session.delete(user)
session.commit()
# 关闭Session:
session.close()
```

上面代码`orm`的增删改查操作

### 创建表

```py
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'news'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


engine = create_engine('mysql+pymysql://root:123456789@localhost:3306/test')
# 创建表
Base.metadata.create_all(engine)
```

### 插入数据

```py
# 插入数据
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 插入数据
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='2', name='ly')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
```

### 查询和更新

```py
# 查询及更新
# 创建session对象:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print ('name:', user.name)
# 更新
user.name = 'hbbaly1314'
print ('name:', user.name)

session.commit()
# 关闭Session:
session.close()
```
### 删除数据

```py
# 删除数据
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()

# 删除
session.delete(user)
session.commit()
# 关闭Session:
session.close()
```

### sqlalchemy 常用方法
```py
1. session.add_all() // 一次添加多条
2. session.rollback() // 回滚
3. query = session.query(User).filter(User.name.like('%ed')).order_by(User.id) // 按照id顺序获取name已ed结尾数据
4. query.all()  // 获取上述全部上句
5. query.first() // 获取第一个
6. query.scalar()  // 调用one（）方法，成功后返回行的第一列
7. for user in session.query(User).filter(text("id<224")).order_by(text("id")).all() // 文本字符串可以灵活地用于查询，方法是指定它们与大多数适用方法都接受的text（）构造一起使用。例如，filter（）和order_by（）
8. session.query(User).filter(User.name.like('%ed')).count()  // 符合条件的个数量
9.query.get(number) // number为第几个，获取第几个
```

# Flask
## 安装
`Mac`系统
```sh
# 1
sudo pip install virtualenv
# 2
mkdir myproject
# 3
cd myproject
# 4
virtualenv venv
# 5
. venv/bin/activate
```

```sh
pip install Flask
```

## 起步

```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

如果你禁用了 debug 或信任你所在网络的用户，你可以简单修改调用 run() 的方法使你的服务器公开可用，如下:

```py
app.run(host='0.0.0.0')`
```
这会让操作系统监听所有公网 IP。

## 调试模式

虽然 `run() `方法适用于启动本地的开发服务器，但是你每次修改代码后都要手动重启它。

调试模式 绝对不能用于生产环境 。

1.
```py
app.debug = True
app.run()
```

2.
```py
app.run(debug=True)
```

```py
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
```

## 路由系统
`route()` 装饰器把一个函数绑定到对应的 `URL` 上。
```py
from flask import Flask
app = Flask(__name__)

# 可以把这些特殊的字段标记为 <variable_name> ， 
# 这个部分将会作为命名参数传递到你的函数。规则可以用 <converter:variable_name> 指定一个可选的转换器。

# int	接受整数
# float	同 int ，但是接受浮点数
# path	和默认的相似，但也接受斜线

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
```

## 构造 URL

`url_for()` 来给指定的函数构造 `URL`。它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。未知变量部分会添加到 URL 末尾作为查询参数。

```py
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

```

## HTTP 方法

`HTTP` （与 `Web` 应用会话的协议）有许多不同的访问 `URL` 方法。默认情况下，
路由只回应 `GET` 请求，但是通过 `route()` 装饰器传递 `methods` 参数可以改变这个行为。

```py
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
```

## 静态文件

动态 web 应用也会需要静态文件，通常是 CSS 和 JavaScript 文件。理想状况下， 
你已经配置好 Web 服务器来提供静态文件，但是在开发中，Flask 也可以做到。 

只要在你的包中或是模块的所在目录中创建一个名为 static 的文件夹，在应用中使用 /static 即可访问
```py
# 给静态文件生成 URL ，使用特殊的 'static' 端点名
url_for('static', filename='style.css')
# 这个文件应该存储在文件系统上的 static/style.css 。
```

## 模板渲染

用 `Python` 生成 `HTML` 十分无趣，而且相当繁琐，因为你必须手动对 `HTML` 做转义来保证应用的安全。为此，`Flask` 配备了 `Jinja2` 模板引擎。

```py
# 你可以使用 render_template() 方法来渲染模板。你需要做的一切就是将模板名和你想作为关键字的参数传入模板的变量。这里有一个展示如何渲染模板的简例:

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)
```

文件放在`templates`文件里面

```js
/templates
    /hello.html
```
