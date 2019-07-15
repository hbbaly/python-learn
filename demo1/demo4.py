# -*- coding: utf-8 -*
# 字符串的操作
# 单引号，双引号，三引号
type('hello world')  # str

"let's go"   # "let’s go"
# \ 转义字符 
'let\'s go'  # "let’s go"

# 多行字符串的处理 '''  , """
''' HBB
HBB
HBB'''
# ' HBB\nHBB\nHBB'
# 上面可以看到每个HBB中件多了个\n  他表示回车键，HBB之间会触发回车键

print(''' HBB
HBB
HBB''')


#  HBB
# HBB
# HBB

# 使用print可以消除\n 的回车键
