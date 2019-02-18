# 面向对象：
# 类的实例化


class Student ():
    name = 'hbb'
    age = 20

    def print_score(self):
        print(self.name, self.age)  # hbb, 20


student = Student()
student.print_score()
