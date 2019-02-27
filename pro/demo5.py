# 对列表中出现的同一个字母做统计
from random import randint
# 第一种方法不推荐
data = [ randint(0,20) for _ in range(20)]  # 随机产生20个大小为0-20的
a = dict.fromkeys(data,0) ## 取出key，默认复制0
print(data)
print(a)
for x in data:
  a[x]+=1

print(a)
# 第二种放方法使用collections Counter方法
from collections import Counter
b = Counter(data)
print(b) # 和a一样
# 找到出现频度最高的三个元素
most_b = b.most_common(3)
print(most_b)