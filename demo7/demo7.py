# -*- coding: utf-8 -*
# 类的多态
class Fa():
    def print_info(self):
        print('this is f')


class S(Fa):
    def print_info(self):
        print('this is s')


s = S()
s.print_info()  # this is s  // 子类和父类有相同的方法，子类覆盖父类
