
# -*- coding: utf-8 -*
# 切片 类似于Slice  从索引0开始取，直到索引n为止，但不包括索引n
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:4])   # ['Michael', 'Sarah', 'Tracy', 'Bob']   ,左闭右开  
# 如果第一个索引是0，还可以省略：
print(L[:4]) 

# 它同样支持倒数切片
print(L[-2:])   # ['Bob', 'Jack']
print(L[-2:-1])  # ['Bob']

# 只写[:]就可以原样复制一个
print(L[:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
H = (1,2,3,4,5,6,7)
print(H[0:5])  # (1, 2, 3, 4, 5)
print(H)   # (1, 2, 3, 4, 5, 6, 7)

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串



