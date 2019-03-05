# 分割字符串
a = 'qwe rtr rweffv rwfer wesdc'
a.split()# 已空格为分割符
print(a.split()) # ['qwe', 'rtr', 'rweffv', 'rwfer', 'wesdc']
# 如歌一个字符串里面多个分隔符，
b = '123;qwer,wwefs| afrv/asdg?vv!'
# 在使用split的话，可能就有点不好
# 可以使用正则表达式
import re
c = re.split(r'[,;|\?/!\t]+', b)
print(c)