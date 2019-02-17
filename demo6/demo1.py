# 模块的导入：import

from demo.demo import *
import demo.demo
print(demo.demo.name)
print(demo.demo.age)  # 20
print(name)
print(age)  # a is not defined

# __all__  中赋值的序列中只对from module_name import 引入模块 有效
