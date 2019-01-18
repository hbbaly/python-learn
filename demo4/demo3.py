#  生成器 ：generator
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
a = (x for x in range(10))
print(a)   # <generator object <genexpr> at 0x00C22570>  不能通过print打印出generate内容

# print(next(a))  # 0
# print(next(a))  # 1
# print(next(a))  # 2
# print(next(a))  # 3
# print(next(a))  # 4
# print(next(a))  # 5
# print(next(a))  # 6
# print(next(a))  # 7
# print(next(a))  # 8
# print(next(a))  # 9
# print(next(a))  # Traceback (most recent call last):


# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素

# 使用for 循环来迭代generate对象
for x in a:
  print(x)

# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：  1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# def fib(max):
#   n,a,b = 0,0,1
#   while n<max:
#     print(b)
#     a,b = b,a+b
#     n +=1
#   return 'done'
# fib(6)


# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

def fib(max):
  n,a,b = 0,0,1
  while n<max:
    yield print(b)
    a,b = b,a+b
    n +=1
  return 'done'

  # fib是一个generate函数，可以直接for循环来迭代
  for x in fib(6):
    print(x)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中