# __slots__: 该class实例能添加的属性
class F():
  __slots__ = ('name', 'age')

class S(F):
  pass

f = F()
s = S()
f.name = 'hbb'
f.age = 20
s.name = 'hbb'
s.age = 20
s.score = 100
print(s.name,s.age,)
print(s.score)
print(f.name,f.age,)
f.score = 100
print(f.score)


#上个例子可以看出 __slots__只能类本身起作用，对子类不起作用