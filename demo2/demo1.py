# -*- coding: utf-8 -*

# 变量

a = [1,2,3,45]  # = 为赋值符号
print(a)   # [1,2,3,45]

# 变量命名 字母数字下划线，，但是首字母不能为数字

# 1a = 'hbb'  # 报错

# 系统关键字也不行


# 变量区分大小写的



a = 1
b = a 
a = 3
print(a, b)   # 3,1

a = [1,2,3]
b = a
a[0] = 'hbb'
print(a, b)   # ['hbb', 2, 3] ['hbb', 2, 3]


# int str tuple 为值类型， list set dict为引用类型

id(a)  # a的变量地址，，，