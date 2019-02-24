a = 0
# def sum (step):
#   sum_step = a + step  # local variable 'a' referenced before assignment
#   a = sum_step
#   return a
# b = sum(2)
# c = sum(5)
# 上面的代码会报错，因为， a = sum_step，表示a是局部变量，sum_step = a + step 中的a还没有赋值，所以就会爆粗

# 使用global解决这个问题
# def sum (step):
#   global a  # gloval表示a是引用全局变量a
#   sum_step = a + step
#   a = sum_step
#   return a
# b = sum(2)
# c = sum(5)
# print(b,c) # 2,7


# 代码中使用全局变量是一件非常不好的现象，可以使用闭包来解决
origin = 0
def no_local(origin): 
  def use_no_local(step):
    nonlocal origin # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
    sum_step = origin + step
    origin = sum_step
    return origin
  return use_no_local
d = no_local(origin)
print(d.__closure__)
print(d.__closure__[0].cell_contents) # 0
print(origin) # 0
print(d(2))
print(d.__closure__[0].cell_contents) # 2
print(origin) # 0
print(d(5))
print(d.__closure__[0].cell_contents) # 7
print(origin) # 0

# origin 没有改变，origin只是在函数use_no_local中改变，记忆总步长, 可以看出d.__closure__[0].cell_contents一直在变，使用的闭包

