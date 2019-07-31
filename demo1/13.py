from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456789@localhost:3306/test')
# 创建对象的基类:
Base = declarative_base()

DBSession = sessionmaker(bind=engine)

class User (Base):
  __tablename__ = 'news'
  # 表的结构:
  id = Column(String(20), primary_key=True, nullable=False)
  name = Column(String(20), nullable=False)
  content = Column(String(200))



class TestNews(object):
  def __init__ (self):
    self.session = DBSession()

  def close_session (self):
    self.session.close()

  def add_one(self):
    new_user = User(id = 1, name = 'hbb', content='测试例子')
    self.session.add(new_user)
    self.session.commit()
    self.close_session()

  def add_all(self):
    new_first_user = User(id=2, name='hbbaly', content='测试例子2')
    new_second_user = User(id=3, name='hbbaly1314', content='测试例子3')
    self.session.add_all([new_first_user, new_second_user])
    self.session.commit()
    self.close_session()

  def query_one (self):
    result_user = self.session.query(User).get(2)
    self.session.commit()

    self.session.refresh(result_user)
    self.session.expunge(result_user)

    self.close_session()
    return result_user
  def query_all(self):
    result_user = self.session.query(User).all()
    for item in result_user:
      print(item.name)
    self.session.commit()
    self.close_session()
    return result_user
    
  def update_one(self):
    result_user = self.session.query(User).get(1)
    result_user.name = 'test'
    self.session.commit()
    self.close_session()
  def delete_one (self):
    result_user = self.session.query(User).get(1)
    self.session.delete(result_user)
    self.session.commit()
    self.close_session()
  def delete_all (self):
    result_user = self.session.query(User).all()
    [self.session.delete(item) for item in result_user]
    self.session.commit()
    self.close_session()

result = TestNews()
# result.add_one()
# result.add_all()
# print(result.query_all())
# result_one = result.query_one()
# print(result_one.name, 'result_one')
# result.update_one()
# result.delete_one()
# result.delete_all()
  