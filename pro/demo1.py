# 过滤掉列表中的负数
from random import randint
import time
a = [randint(-10,10) for _ in range(10)] # 生成一个含有10位的列表
# 1.使用filter来解决
b = filter(lambda x:x>=0,a)
print(a)
print(list(b))
# 2.使用列表解析来解决
c = [x for x in a if x>=0]
print(c)


# 这两种方式我们首选列表解析，因为它运行的时间更短，
st = time.time()
filter(lambda x:x>=0,a)
et = time.time()
se = et-st
print(se)
st1 = time.time()
[x for x in a if x>=0]
et1 = time.time()
print(et1-st1)