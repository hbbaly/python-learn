# 跑出错误
def is_zero(val):
  if val == 0:
    raise ValueError('传递参数不能为0')

is_zero(0)
# Traceback (most recent call last):
#   File "demo3.py", line 6, in <module>
#     is_zero(0)
#   File "demo3.py", line 4, in is_zero
#     raise ValueError('传递参数不能为0')
# ValueError: 传递参数不能为0