# 条件判断
age = 20
if age <= 20:
  print(age)     # 20


if age > 20:
  print('adult')
else:
  print('teenager')   # teenager


if age > 18:
  print('adult')
elif age > 6:
  print('teenager')
else:
  print('kid')



s = input('birth:')
birth = int(s)
if birth <2000:
  print('90后')
else:
  print('00后')
