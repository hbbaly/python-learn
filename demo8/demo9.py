# re.sub: 吧匹配成功的进行替换 re.sub(partten, replace, str,const)
import re
a = 'pythonc++pythonjspythonjava'
b = re.sub('python', 'hbb', a)
print(b)  # hbbc++hbbjshbbjava
# 第四个参数; 默认是0表示全部替换
c = re.sub('python', 'hbb', a, 1)
d = re.sub('python', 'hbb', a, 0)
e = re.sub('python', 'hbb', a, 2)
print(c)  # hbbc++pythonjspythonjava
print(d)  # hbbc++hbbjshbbjava
print(e)  # hbbc++hbbjspythonjava


# 第二个参数可以为函数：
def convert_val(value):
    print(value.group())  # 打印三次python
    return '!!'+value.group()+'!!'


f = re.sub('python', convert_val, a)
print(f)  # !!python!!c++!!python!!js!!python!!java
