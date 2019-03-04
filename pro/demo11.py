# 如何在for循环中迭代多个可迭代的对象
# 求每个学生的总分：
from random import randint
from itertools import chain
math = [randint(60,100) for _ in range(40)]
english = [randint(60,100) for _ in range(40)]
chinese = [randint(60,100) for _ in range(40)]
# // 第一种方法
for score in range(len(math)):
  print(score ,math[score]+english[score]+chinese[score])
# 第二种方法
sum = []
for a,b,c in zip(math,chinese,english):
  sum.append(a+b+c)
print(sum)
# 链式拼接，可迭代的拼接在一起
a = [1,2,3]
b = ['q','w','e','r']
c= chain(a,b)
for a in c:
  print(a)
print(c)

Sum = chain(math,english,chinese)
count = 0
for x in Sum:
  if x>90:
    count+=1
print(count)   # 三个班的人成绩大于90的
