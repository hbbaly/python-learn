# 迭代
# list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 迭代是通过for ... in来完成的

# list , dict, str

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
True
isinstance([1,2,3], Iterable) # list是否可迭代
True
isinstance(123, Iterable) # 整数是否可迭代
False