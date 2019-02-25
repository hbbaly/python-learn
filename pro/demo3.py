# 集合筛选,筛选出集合中能被3整除的数
from random import randint
a = [randint(-10,10) for _ in range(10)]
b = set(a)
c = {x for x in b if x%3==0}
print(c)