# 判断字符串已某个字符结尾或者开始
# str.startswith,str.endswith
import os, stat
print(os.listdir('.')) # 获取当前目录下的文件
# 先做个简单的测试
a = 'jquery.js'
AS = a.startswith('jquery')
print(AS)  # True
As = a.endswith('js')
print(As) # True
os_list = [x for x in os.listdir('.') if x.endswith('js') ]
print(os_list)  # ['jquery.js']
os_mode = os.stat('jquery.js').st_mode
print(os_mode)

os.chmod('jquery.js',os.stat('jquery.js').st_mode|stat.S_IXUSR)