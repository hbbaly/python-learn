# -*- coding: utf-8 -*
# 循环
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
arr = [1,2,3,4,5,6]
for item in arr:
  print(item)

sum = 0
for item in arr:
  sum += item

print(sum)


# range()函数  可以生成一个整数序列，再通过list()函数可以转换为list。
arr = list(range(6))   # 从0开始  [0, 1, 2, 3, 4, 5]
print(arr)


# break语句可以提前退出循环
n = 0
while n <= 100:
  if n > 10:
    break
  print(n)
  n += 1
print('end',n)


# continue语句，跳过当前的这次循环，直接开始下一次循环。

n = 0
while n < 10:
  n += 1
  if n%2== 0:
    continue
  print(n)  # 1 3 5 7 9
