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
  def close_connect(self):
    self.connect.close()
  # 
  def createDb(self, sql):
    self.__isExsistDb__()
    self.cursor.execute(sql)
    self.close_connect()

  def __isExsistDb__(self):
    self.cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

  def findData(self, sql, type="all"):
    self.cursor.execute(sql)
    data = ''
    if type == "all":
      data = self.cursor.fetchall()

    else:
      data = self.cursor.fetchone()
      # 获取的数组转为字典
      data = [dict(zip([item[0] for item in self.cursor.description], data))]
    self.connect.commit()
    self.close_connect()
    # data是一个元祖
    
    return data
  def insert_data(self, sql):
    self.cursor.execute(sql)
    self.connect.commit()
    self.close_connect()
  def update_data(self, sql):
    self.cursor.execute(sql)
    self.connect.commit()
    self.close_connect()
  def delete_data(self, sql):
    self.cursor.execute(sql)
    self.connect.commit()
    self.close_connect()
sql = """CREATE TABLE EMPLOYEE (
  FIRST_NAME  CHAR(20) NOT NULL,
  LAST_NAME  CHAR(20),
  AGE INT,  
  SEX CHAR(1),
  INCOME FLOAT )"""
test = DB()
# print(test.createDb(sql))

findOneSql = "SELECT * FROM `test`.`user`"
update_sql = """UPDATE `EMPLOYEE` SET AGE = AGE + 18"""
insert_sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Macb', 'Mo', 20, 'M', 20000)"""
delete_sql = """DELETE FROM `EMPLOYEE` WHERE AGE > 30"""
# print(test.findData(findOneSql, 'one'))
# print(test.update_data(update_sql))
# print(test.insert_data(insert_sql))
print(test.delete_data(delete_sql))

# 增删改查
