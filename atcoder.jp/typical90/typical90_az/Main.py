import math
import itertools

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

ans = 1
for i in range(n):
  ans = ans * sum(a[i])
print(ans % (pow(10, 9) + 7))
