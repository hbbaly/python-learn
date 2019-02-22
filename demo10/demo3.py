import os
print(dir(os))
print(os.name) # posix # 操作系统类型
print(os.uname()) # 取详细的系统信息
print(os.environ) # 环境变量
# 要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('TERM_PROGRAM'))  # vscode

# # 查看当前目录的绝对路径
print(os.path.abspath('.')) # /Users/hanbingbing/Desktop/code/github/python-learn/demo10

# md = os.mkdir('/Users/hanbingbing/Desktop/code/github/python-learn/demo11')
os.rmdir('/Users/hanbingbing/Desktop/code/github/python-learn/demo11')
# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')
alld= [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(alld)