# map
a = range(1,9)
def square_a(a):
  b = a*a
  return b
for x in a:
  c = square_a(x)
  print(c)

d = map(square_a, a)
print(list(d))  # [1, 4, 9, 16, 25, 36, 49, 64]

# map(func, itera)  两个参数，第一个为函数，第二个为 每一项