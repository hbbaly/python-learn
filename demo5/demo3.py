# -*- coding: utf-8 -*
# range()生成序列
a = range(0, 10)   # 生成[0,1,2,3,4,5,6,7,8,9]
for x in a:
    print(x)
# range(a, b, c)  c为步长
for x in range(0, 10, 3):
    print(x)
# 如果生成倒序的
for x in range(10, 0, -3):
    print(x)
# 序列中的所有的数组合一列并且以|拼接
for x in a:
    print(x, end = '|')
# 0|1|2|3|4|5|6|7|8|9|
