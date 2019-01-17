# 迭代
# list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 迭代是通过for ... in来完成的

# list , dict, str

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

# from collections import Iterable
# isinstance('abc', Iterable) # str是否可迭代
# True
# isinstance([1,2,3], Iterable) # list是否可迭代
# True
# isinstance(123, Iterable) # 整数是否可迭代
# False


#  列表生成式

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
print(list(range(0,10)))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 左闭右开

# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
l=[]
for x in range(1,11):
  l.append(x*x)
print(l)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  

# 更加简单方法:  列表生成式
print([x*x for x in range(1,11)])

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]   写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用

# for循环后面还可以加上if判断，
print([x*x for x in range(1,11) if x%2==0])  # [4, 16, 36, 64, 100]

# 还可以使用两层循环，可以生成全排列：
print([m+n for m in 'asdf' for n in 'qwer'])
# ['aq', 'aw', 'ae', 'ar', 'sq', 'sw', 'se', 'sr', 'dq', 'dw', 'de', 'dr', 'fq', 'fw', 'fe', 'fr'] 16中组合


##### 列出当前目录下的所有文件
import os
print([d for d in os.listdir('.')])   # ['demo1.py', 'demo2.py']


# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value

# items() 函数以列表返回可遍历的(键, 值) 元组数组。
d = {'a':'b','c':"d", 'e':'f'}
print(d.items())   # dict_items([('a', 'b'), ('c', 'd'), ('e', 'f')])
for k,v in d.items():
  print(k,'=', v)

# a = b
# c = d
# e = f

print([a+'='+b for a,b in d.items()])   # ['a=b', 'c=d', 'e=f']
print([s.upper() for s in d])    # ['A', 'C', 'E']