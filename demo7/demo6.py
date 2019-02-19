# 类的继承
class Fa():
    def print_info(self):
        print('this is f')


class S(Fa):
    def print_name(self):
        print('S')


s = S()
s.print_info()  # this is f
s.print_name()  # S
