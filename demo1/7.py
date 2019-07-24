import pymysql

class DB() :
  def __init__(self, host="localhost", root = 'root',  password="123456789", base='test'):
    # 建立链接
    self.connect = pymysql.connect(host, root, password, base)
    # 创建游标对象
    self.cursor = self.connect.cursor()
  # 返回游标
  def __enter__(self):
    return self.cursor

  # 
  def createDb(self, sql):
    self.__isExsist__()
    self.cursor.execute(sql)
    self.connect.commit()
    self.connect.close()

  def __isExsist__(self):
    self.cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
  FIRST_NAME  CHAR(20) NOT NULL,
  LAST_NAME  CHAR(20),
  AGE INT,  
  SEX CHAR(1),
  INCOME FLOAT )"""
test = DB().createDb(sql)
print(test)
