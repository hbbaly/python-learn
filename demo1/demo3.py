# -*- coding: utf-8 -*
# boolean  True False  ，都是首字母大写，小写会报错。
print(True)   # True
print(False)  # False

type(True)  # bool
type(False) # bool

# ##### 为什么bool会归类到Number类型中：
int(True)   # 1
int(False)  # 0

bool(1)  # True
bool(0) # False


# 除了0可以表示False，'',[],{}，None也可以表示为False

a = 444444;b = 444444

print(a is b)