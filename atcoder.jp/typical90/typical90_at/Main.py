import math
import itertools

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_b = {}

a = [ v % 46 for v in a ]
b = [ v % 46 for v in b ]
c = [ v % 46 for v in c ]

a_map = {}
b_map = {}
c_map = {}

for i in range(n):
  a_map[a[i]] = a_map.get(a[i], 0) + 1
for i in range(n):
  b_map[b[i]] = b_map.get(b[i], 0) + 1
for i in range(n):
  c_map[c[i]] = c_map.get(c[i], 0) + 1

ans = 0
  
for i in range(46):
 for j in range(46):
  for k in range(46):
    if (i + j + k) % 46 == 0:
      ans += a_map.get(i, 0) * b_map.get(j, 0) * c_map.get(k, 0)

print(ans)
