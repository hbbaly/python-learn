# 作用域
def f ():
  a = 10
  def s ():
    a = 20  # 和外面a不是同一个，不受外面a的影响，python认为这里的a是一个s函数的局部变量
    print(a)
  print(a)
  s()
  print(a)
f()
# 和js有作用域