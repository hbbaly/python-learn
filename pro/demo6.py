# 根据字典中的值，对字典进行排序
# 第一种方法sorted推荐使用
from random import randint
a = {x:randint(60,100) for x in 'qwertyuio'}
b = a.items() # 元祖 
print(b)
c = sorted(b, key=lambda x : x[1],reverse=True)  # True 从大到小，False从小到大
print(c)


# 第二种方法
e = a.keys()
f = a.values()
g = zip(f,e)  # sorted 是按照第一个来排序的，所以把key，value转换称一个元祖
h = sorted(g,reverse=True)
print(h)