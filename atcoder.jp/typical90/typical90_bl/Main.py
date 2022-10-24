import math
import itertools

n, q = map(int, input().split())
a = list(map(int, input().split()))
diff = []
ans = 0
for i in range(1, n):
  diff.append(a[i] - a[i - 1])
ans = sum([abs(v) for v in diff])

for i in range(q):
  l, r, v = map(int, input().split())

  before_diff = 0
  after_diff = 0
  if l > 1:
    before_diff += abs(diff[l - 2])
    diff[l - 2] += v
    after_diff += abs(diff[l - 2])
  if r < n:
    before_diff += abs(diff[r - 1])
    diff[r - 1] -= v
    after_diff += abs(diff[r - 1])

  ans += after_diff - before_diff
  print(ans)
