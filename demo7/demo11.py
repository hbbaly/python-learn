# 使用枚举类型
from enum import Enum, unique
@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# 对应的key value
print(weekday.Mon)  #  weekday.Mon
print(weekday.Mon.value) # 1