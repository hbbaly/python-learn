# 边界匹配
# ^, $   ^以起始    $以结尾
import re
a = '100023400000001'
b = re.findall(r'^000', a)
c = re.findall(r'001$', a)
d = re.findall(r'^000$', a)
print(b)  # []
print(c)  # ['001]
print(d)  # []
