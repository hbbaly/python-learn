# -*- coding: utf-8 -*
# 逻辑运算符

# and or not  
# 逻辑运算符并不是返回的是bool   也有可能是某个为True的只


print('a' and 'b')  # 'b'

'a' or 0  # 'a'
 
# 成员运算符  : 一个元素是否在另一个元素中   返回的是bool

# in  not in


# 字典中的 成员运算符是key：value来进行的 

b= 'hbb'
b in {'name':'hbb'}  # 都被认为False

b = 'name'
b in {'name':'hbb'}  # True

# 身份运算符  : 如果两个变量身份(内存地址)是否相等  返回bool

# is  is not 

# is  与 == 区别

a = 1
b = 1
a == b  # True
a is b  # True


a = 1
b = 1.0
a == b  # True
a is b  # False

a = {1,2}
b = {2,1}
a == b  # True  集合是无序的，所以比较值是相等的

a is b # False

a = [1,2]
b = [2,1]
a == b  #False
a is b # False

a = (1,2)
b = (2,1)
a == b # False
a is b # False


# 0  '' [] () {} 都被认为False


# 判断类型

# isinstance()

a = 'hbb'
isinstance(a,str)  # True

isinstance(a,(str,int,bool))  #True

isinstance(a,(int,bool))  # False

