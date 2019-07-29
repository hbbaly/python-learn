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
# Base.metadata.create_all(engine)

# 插入数据
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 查询
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print ('name:', user.name)
# 关闭Session:
session.close()
