# 多个字典中的公共建
from random import randint, sample
a = {x:randint(1,5) for x in sample('qwertyuiop',randint(4,6))}
b = {x:randint(1,5) for x in sample('qwertyuiop',randint(4,6))}
c = {x:randint(1,5) for x in sample('qwertyuiop',randint(4,6))}
# 第一种办法.,比较小的时候
d = a.viewkeys()&b.viewkeys()&c.viewkeys()

# 第二种map与reduce结合
h = map(dict.viewkeys,[a,b,c])
f = reduce(lambda x,y:x & y,h)
print(f)
print(h)