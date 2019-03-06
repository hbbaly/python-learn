# 字符串的拼接
a = 'hbba'
b = 'ly'
c = a+b
print(c)

# 要拼接可迭代对象
d = ['qwe','asds','xfsdg','fdweg']
s = ''
for item in d:
  s+=item

print(s)
# 着中for循环写法浪费性能，可以用str.join()来写
f = ''
e = f.join(d)
print(e)