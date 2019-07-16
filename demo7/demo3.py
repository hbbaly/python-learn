# -*- coding: utf-8 -*
# __init__的用法
# __init__在类实例化的时候会自动执行， 可以在这里利用实例化传的参数对类的属性进行修改


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
print(student.name, student.age)
