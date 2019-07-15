# -*- coding: utf-8 -*
# 字典 dict  

type({'name':'hbb','age':18,'sex':1})   # dict

# 字典的访问方式  
# 通过key 来访问value
{'name':'hbb','age':18,'sex':1}['name']   # 'hbb

# 字典没有重复的键
{(1,2):'hbb'}  # 没有报错
# 字典的键 key必须是不可变的类型  int str tuple ,但是列表 dist, set,不行

# 会报错
# {[1,2]:'hbb'}  #  unhashable type: 'list'
# {{1,2}:'hbb'}   #  unhashable type: 'set'

