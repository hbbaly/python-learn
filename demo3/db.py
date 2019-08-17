# -*- coding: utf-8 -*-
# 链接数据库
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@127.0.0.1:3306/test'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "flask"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

class Test ():
  def __init__(self):
    self.db  = db

  def connect_close(self):
    self.db.session.commit()

  def add_one(self):
    user = User('prete', 'prete@example.com')
    self.db.session.add(user)
    self.connect_close()

  def query_all(self):
    list = User.query.all()
    return list

  def query_one(self):
    user = User.query.get(2)
    return user

  def delete_one(self):
    user = User.query.get(2)
    self.db.session.delete(user)
    self.db.session.commit()

  def update_one(self):
    user = User.query.first()
    user.username = 'hbb'
    self.db.session.commit()

  def filter_user(self):
    user = User.query.filter_by(username='hbb').first()
    return user
  def limit_user(self):
    user = User.query.limit(2).all()
    return user