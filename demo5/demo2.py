# -*- coding: utf-8 -*
# for else 应用 序列， 集合， 字典
arr = [1, 2, 3, 4, 5]
for x in arr:
    if(x == 3):
        break    # break 打断这次循环， else也不执行
    print(x)
else:
    print('EOF')
for x in arr:
    if(x == 3):
        continue  # continue 只中断当 x = 3的循环，并且else也会继续执行
    print(x)
else:
    print('EOF')
# for 循环也可以嵌套
arr1 = [[1, 2, 3], (4, 5, 6)]
for x in arr1:
    for y in x:
        print(y)
