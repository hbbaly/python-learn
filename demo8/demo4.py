# * 匹配0次，多次
import re
a = 'javf123java456javaaaa'
b = re.findall('java*', a)
print(b)  # ['jav', 'java', 'javaaaa']
# + 匹配1次或者无限多次
c = re.findall('java+', a)
print(c)  # ['java', 'javaaaa']

# 匹配0次或1次
d = re.findall('java?', a)
print(d)  # ['jav', 'java', 'java']
