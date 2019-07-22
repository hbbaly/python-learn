# 序列反向
a = [1,4,3,2,5,6]
b = reversed(a)
for x in b:
  print(x)

class Float_range:
  def __init__(self, start, end, step=0.1):
    self.start = start
    self.end = end
    self.step = step
  def __iter__(self):
    st = self.start
    while st<=self.end:
      yield st
      st+=self.step
  def __reversed__(self):
    et = self.end
    while et>=self.start:
      yield et
      self.end-=self.step

for x in Float_range(1.0,5.0,0.5):
  print(x)

# for y in reversed(Float_range(1.0,5.0,0.5)):
#   print(y,'=====reversed====')