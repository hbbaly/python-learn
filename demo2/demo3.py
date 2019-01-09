# 赋值运算符

# = += *= /= %= **= //=

a = 1

a+=2  # 3

a*=2  # 6

a /=2  # 3

a = 5 
a%=3   # 2

2**=4  # 16

5//=3  # 1




# 关系运算符

 # == != > < >= <=

a = 1
b = 2

print(a==b)   # False


print(1!=2)  # True
print(1>2)


# 如果 int float 与 bool相加，， True会转化为1  False ： 0

# > <  
# 单个字符串比较是以ascii码作为比较，，，字符串长度大于1，从第一个开始比较

'hbb'>'abc'  # T rue
'hbb'<'a'   # False
'hbb'<'w'   # True
 