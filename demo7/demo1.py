# -*- coding: utf-8 -*
# 函数返回多个结果的写法
def result(a, b, c):
    return a, b, c


e, f, g = result(1, 2, 3)  # 类似与es6的结构赋值
print(e, f, g)  # 1,2,3
