# -*- coding: utf-8 -*
# 转译字符
# \'   \n   \t

# 输出一个文件夹的路径
print('C:python\npython-learn')
# C:python
# python-learn

# 如果想要输出 'C:python\npython-learn'

print('C:python\\npython-learn')

# 也可以使用这种方式,来代替转译字符，字符串前面加上r，表示原始字符串，即所见即所得
print(r'C:python\npython-learn')

# print(r'let's go')   # 这种类型例外，会报错，因为都不是字符串了