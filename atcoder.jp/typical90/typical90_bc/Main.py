import math
import itertools


n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for v in itertools.combinations(a, 5):
  v1, v2, v3, v4, v5 = v
  tmp = v1 % p
  tmp = (tmp * v2) % p
  tmp = (tmp * v3) % p
  tmp = (tmp * v4) % p
  tmp = (tmp * v5) % p
  if tmp % p == q:
    ans += 1

print(ans)