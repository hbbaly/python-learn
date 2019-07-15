# -*- coding: utf-8 -*
# 函数基础知识

# Python内置了很多有用的函数，我们可以直接调用
# abs()  # 求绝对值：接受一个参数
abs(10)  # 10
abs(-10) # 10
#  abs('10') # 参数类型不能被函数所接受，也会报TypeError的错误  bad operand type for abs(): 'str'


# max  :max()可以接收任意多个参数，并返回最大的那个
max(1,2,3,4)   #4
# max(1,2,3,'hbb','d')   # not supported between instances of 'str' and 'int'


# 数据类型转换

# python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数，str()转化str，bool转化为bool