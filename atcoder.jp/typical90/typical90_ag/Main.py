# TODO edit this code, this code is for https://atcoder.jp/contests/practice/tasks/practice_1
import math
# param

h, w = map(int, input().split())
if h == 1 or w == 1:
  ans = h * w
else:
  ans = math.ceil(h / 2) * math.ceil(w / 2)

print(ans)
