import math
import itertools

n, m = map(int, input().split())
adjacency_list = [[] for _ in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  adjacency_list[a-1].append(b-1)
  adjacency_list[b-1].append(a-1)

ans = 0

for i in range(n):
  cnt = 0
  for j in adjacency_list[i]:
    if i > j:
      cnt += 1
  if cnt == 1:
    ans += 1
print(ans)

