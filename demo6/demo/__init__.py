# __init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件。
# 我们可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入。
import os
import sys
__all__ = ['os']
a = 'this is first step'
print(a)
