# -*- coding: utf-8 -*
# 正则表达式
import re
a = 'abc,adc,aec,afc,agc,ahc,asc'
b = re.findall('a[bde]c', a)  # 找出中间字母为b或者d或者e的
print(b)  # ['abc', 'adc', 'aec']
c = re.findall('a[^bde]c', a)  # ['afc', 'agc', 'ahc', 'asc']  和'a[bde]c'作用相反
print(c)
d = re.findall('a[b-e]c', a)  # 找出
print(d)  # ['abc', 'adc', 'aec']

# '\d'可以用[0-9]代替
# '\D'可以用[^0-9]代替
# ‘\w'数字字母_  可以用[A-Za-z0-9_]
