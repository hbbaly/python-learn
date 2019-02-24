# reduce python3中reduce已经不再全局命名空间里面
from functools import reduce
a = range(1,6)
# 列表元素只和
b = reduce(lambda x,y: x+y,a)
print(b)  # 15
#   求list中的元素乘积
c = reduce(lambda x,y:x*y,a)
print(c)  # 120
# 稍微有点难度的  有初始化值的情况, 这个时候就不是取列表的前两项, 而是取初始值为第一个,序列的第一个元素为第二个元素,开始进行lambda函数的应用计算.
d = reduce(lambda x ,y: x+y,a ,5)
print(d) # 20
e = reduce(lambda x,y:x*y, a, 5)
print(e) # 600