# 访问限制：


class Student ():
    name = ''
    age = 0

    def __init__(self, name, age):
        print('__init__', name, age)
        self.name = name
        self.age = age

    def print_score(self):
        print(self.name, self.age)  # hbb, 20


student = Student('hbb', 20)
student.name = 'ly'
student.age = 18

print(student.name)   # ly
print(student.age)    # 18

# 外部可以更改类内部的属性
# 我们可以使用__来标识就变成了一个私有变量，


class Teacher ():
    __name = ''
    __age = 0

    def __init__(self, name, age):
        print('__init__', name, age)
        self.__name = name
        self.__age = age

    def print_score(self):
        print(self.__name, self.__age)  # hbb, 20


teacher = Teacher('hbb', 20)

print(teacher.__name)   # 报错，已经访问不到__name, __age
