# -*- coding: utf-8 -*
# 递归函数

def fact(n):
  if(n==1):
    return 1
  return n*fact(n-1)
print(fact(3))  # 6
print(fact(5))  # 120 
# print(fact(1000))   ##  栈溢出

# 尾递归优化
def Fact(n):
  return fact_iter(n,1)

def fact_iter(num,product):
  if(num == 1):
    return product
  return fact_iter(num-1,num*product)

print(Fact(3))  # 6
print(Fact(5))  # 120 
print(Fact(1000))   # 也会导致栈溢出