# 对迭代器进行切片
from itertools import islice
f = open('./jquery.js')
for line in islice(f,100,105):
  print(line)


  # islice会改变原来的**迭代器**

a = range(20)
a = iter(a)  # 没有这一步进行islice a是不会改变
for x in islice(a,5,10):
  print(x,'============')
for y in a:
  print(y,'----------')