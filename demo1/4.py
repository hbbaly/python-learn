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

print(data)
 
# 关闭数据库连接
db.close()