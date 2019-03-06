# 字符串的左右，剧中对齐
# str.ljust,str.rjust,str.center
a = 'hbbaly'
al = a.ljust(20)
print(al)
ad = a.ljust(20, '=')
print(ad)
ar = a.rjust(20)
print(ar)
ard = a.rjust(20,'=')
print(ard)
ac = a.center(20)
print(ac)
acd = a.center(20,'=')
print(acd)

# 使用format方法
q = format(a,'<20')  #做对其
w = format(a,'>20')  # 又对其
e = format(a,'^20')  # 剧中对其

d = {
  'asvg':'qwefrg',
  'qwerewgrfvd':'adfv',
  'wrtyt':'frgb',
  'wrgvdcawefr':'rggt'
}
# 让字典dkey属性左对齐
key = d.keys()  # 获取d中key
key_len = map(len,key) # 获取每个key值长度
key_len_max = max(key_len) # 获取key值长度最大值
s = []
for item in d:
  s.append({item.ljust(key_len_max):d[item]})