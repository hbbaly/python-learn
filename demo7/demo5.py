#  __使用在外部获取不到类的属性，我们可以增加set， get
class Teacher ():
    __name = ''
    __age = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name


teacher = Teacher('ly', 18)
print(teacher.get_name)  # ly
set_name = teacher.set_name('hbb')
print(set_name)  # hbb
