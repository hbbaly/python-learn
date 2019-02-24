# 匿名函数
def add (x, y):
  return x+y
a = add(1,2)
print(a) # 3

# 使用lambda表示匿名函数，其中冒号后面的必须是表 达式，表达式   表达式
b = lambda x, y: x+y
c = b(1, 2)
print(c) # 3
# 三元表达式    为真时的值 if 条件判断 else 为假时的值
d = lambda x,y: x+y if x+y>5 else y
e = d(2,2)
f = d(3,4)
print(e)
print(f)