import math
import itertools

q = int(input())
txs =[list(map(int, input().split())) for _ in range(q)]

mnt = []
for i in range(q):
  t, x = txs[i]
  if t == 1:
    mnt.insert(0, x)
  elif t == 2:
    mnt.append(x)
  else:
    print(mnt[x - 1])