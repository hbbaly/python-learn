# 调整字符串中的中文文本格式
# 2019-03-05 变成 03/05/2019
import re
a = '2019-03-05'
b = re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',a)  
print(b)  # 03/05/2019

c = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',a)
print(c) # 03/05/2019