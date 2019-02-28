# 晒选出字典中某个属性高于80的项
from random import randint
a = {x:randint(60,100) for x in range(1,21)}
print(a.items())
b = {k:v for k,v in a.items() if v>85}
print(b)
