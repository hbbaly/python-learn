# 让字典变得有序 OrderedDict
from time import time
from random import randint
from collections import OrderedDict
d = OrderedDict()
start = time()
players = list('abcdefgh')
for i in range(8):
  p = players.pop(randint(0,7-i))
  end = time()
  d[p] = (i+1, end-start)

for k in d:
  print(d,'=-=======',d[k])