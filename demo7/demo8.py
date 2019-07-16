# -*- coding: utf-8 -*
# 判断一个对象是否是函数：
import types  # ['AsyncGeneratorType', 'BuiltinFunctionType', 'BuiltinMethodType', 'ClassMethodDescriptorType', 'CodeType', 'CoroutineType', 'DynamicClassAttribute', 'FrameType', 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'LambdaType', 'MappingProxyType', 'MemberDescriptorType', 'MethodDescriptorType', 'MethodType', 'MethodWrapperType', 'ModuleType', 'SimpleNamespace', 'TracebackType', 'WrapperDescriptorType', '_GeneratorWrapper', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ag', '_calculate_meta', 'coroutine', 'new_class', 'prepare_class', 'resolve_bases']


def getsdv():
    pass


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir(types))
type(getsdv) == types.FunctionType  # True

# 使用isinstance()


class Fa():
    def print_info(self):
        print('this is f')


class S(Fa):
    name = 'hbbaly'
    def print_info(self):
        print('this is s')

    def set_name (self):
        self.name = 'hbbaly1314'

print(dir(S))  # ['__doc__', '__module__', 'name', 'print_info', 'set_name']
a = Fa()
b = S()
print(isinstance(a, Fa))  # True
print(isinstance(b, Fa))  # True
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”
