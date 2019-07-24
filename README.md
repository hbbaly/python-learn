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
