from logging import root
import math
import itertools

n = int(input())
root_n = math.floor(math.sqrt(n))

nums = []
for i in range(2, root_n + 1):
  while n % i == 0:
    n = n // i
    nums.append(i)
if len(nums) == 0:
  print(0)
else:
  if n > root_n:
    nums.append(n)
  cnt = 1
  while pow(2, cnt) < len(nums):
    cnt += 1
  print(cnt)


