import math
import itertools

n, k = map(int, input().split())
arr = []
for i in range(n):
  a, b = map(int, input().split())
  arr.append(b)
  arr.append(a - b)

arr.sort(reverse=True)

print(sum(arr[0:k]))
