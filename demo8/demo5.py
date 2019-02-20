# match使用
import re
a = '023-5803511'
# 建议使用Python的r前缀，就不用考虑转义的问题了
b = re.match(r'\d{3}\-\d+$', a)
if b:
    print('此电话号码符合')
else:
    print('None')

# 切分字符 split
c = re.split(r'[\,\s]', 'a,a,c,d b g h')  # 以, 空格拆分字符串
print(c)  # ['a', 'a', 'c', 'd', 'b', 'g', 'h']
# 提取 group
d = re.match(r'(^\d{3})-(\d+$)', a)   # ()-()分成了两组 从匹配的字符串中提取出区号和本地号码
print(d.group(0))  # 023-5803511  group(0)永远是原始字符串
print(d.group(1))  # 023
print(d.group(2))  # 5803511  group(1)、group(2)……表示第1、2、……个子串
