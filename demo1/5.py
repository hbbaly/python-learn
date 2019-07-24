# 更新数据
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