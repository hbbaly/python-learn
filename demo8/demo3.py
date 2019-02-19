# 数量词, 默认是贪婪模式，在满足情况下尽可能取多的
import re
a = 'asdf123efe456g'
b = re.findall('[a-z]{3}', a)
print(b)  # ['asd', 'efe']  # 取三个连续的字符

c = re.findall('[a-z]{3,6}', a)
print(c)  # ['asdf', 'efe']
d = re.findall('[a-z]{3,6}?', a)  # ?为非贪婪
print(d)  # ['asd', 'efe']
e = re.findall('[a-z]{2,}', a)
print(e)  # ['asdf', 'efe'] 至少取两个连续的字符
