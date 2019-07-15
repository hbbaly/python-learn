# -*- coding: utf-8 -*
# 字符串的操作

# len()
len('hello world')   # 11 长度11

 # 字符串的拼接

'hello ' + 'world'  # 'hello world'

# *  

'hello'*2  # 是把字符串重复2次，'hellohello'

'hello'*0  # ' ' 

# 获取字符串中的某一个字符

'hello world'[0]  # 'h'
'hello world'[3]  # 'l'
# [n]表示从字符串下表为0开始到n，n所对应的字符， [-n]表示从字符串的末尾数n次所对应的字符
'hello world'[-1]  # 'd'
'hello world'[-2]  # 'l'

# 截取字符串的某一段字符

'hello world'[0:3]  # 'hel'
'hello world'[1:5]  # 'ello'

# [a:b]从a下标所对应的字符到b下表所对应的字符，之间的字符串，不包括b对应的字符

'hello world'[0:-3]  # 'hello wo'
'hello world'[1:-5]  # 'ello '

# :后面没有数字或者过大，都表示到末尾。
'hello world'[1:]  # 'ello world'
'hello world'[1:18]  # 'ello world'
'hello world'[-4:]  # 'orld'