# 闭包： 内部函数使用了外部函数的变量
def f ():
  a = 10
  def s ():
    return a^2
  return s
b = f()
print(b.__closure__)  # b有 __closure__ 这个属性，说明有闭包现象的存在：
print(b.__closure__[0].cell_contents)  # 10 打印了闭包使用的变量