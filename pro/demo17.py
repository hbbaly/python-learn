# 去掉不用的字符串
# str。strip（）去掉两端空白， str.lstrip()去掉左端空白，str.rstrip（）去掉右端空白
a = '  sd gb  '
print(a.strip())
a = '  sd gb  '
print(a.lstrip())
a = '  sd gb  '
print(a.rstrip())

# 去掉中间的： 可以切片，split（），
b = '21314:efgb'
c = b[:5]+b[-4:]
print(c)
# 使用字符串的replace
d = b.replace(':','')
print(d)

# 使用re.sub去除
import re
b = '21314:efgb'
e = re.sub(r':','',b)
print(e)


# str.translate()
# from string import maketrans   # python3.4没有maketrans这个属性了
f = 'abc12346xyz'
r = f.maketrans('abcxyz','xyzabc')  # 映射列表，把a=>x,b=>y,c=z,x=>a.......
print(f.translate(r))  # xyz12346abc