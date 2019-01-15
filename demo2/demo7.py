# dict set 补充

#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

# dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
a = {'name':'hbb', 'age':20}
a.get('sex')   # None 在python中不显示


# 可以指定返回值

print(a.get('sex', 'hbb'))  # 'hbb



# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
a.pop('name')
print(a)   # {'age':20}

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。


# set 由于key不能重复，所以，在set中，没有重复的key

s = set([1,2,3,4,1,2,3])
print(s)     # {1,2,3,4}


# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果

s.add(5)
s.add(6)
print(s)

# 通过remove(key)方法可以删除元素：

s.remove(6)
s.remove(5)
print(s)  # {1,2,3,4}

# 可变元素
a = ['3', '2', '1']
a.sort()
print(a)   # 1,2,3

# 不可变
string = 'abc'
string.replace('a', 'A')
print(string)   # abc