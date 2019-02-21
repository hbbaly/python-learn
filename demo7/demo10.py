# @ property: 给函数动态添加功能
class Student(object):
  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    self._score = value

s = Student()
s.score = 99
print(s.score)

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class S():
  @property
  def score(self):
    return self._score
  @score.setter
  def score(self, value):
    self._score = value
  @property
  def age(self):
    return self._score

s = S()
s.score = 100
print(s.age)