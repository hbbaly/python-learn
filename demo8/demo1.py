# -*- coding: utf-8 -*
# 正则表达式

import re
print(dir(re))
a = '1c2c++3c#4python5js6java78go'
b = re.findall('python', a)  # ['python']吧符合条件的组合成序列
if len(b) > 0:
    print('python')
else:
    print('No')

c = re.findall('\d', a)  # \d为元字符， 找到所有的数字
d = re.findall('[^0-9]', a)
print(c, d)  # ['1', '2', '3', '4', '5', '6', '7']['c', 'c', '+', '+', 'c', '#', 'p', 'y', 't', 'h', 'o', 'n', 'j', 's', 'j', 'a', 'v', 'a', 'g', 'o']
