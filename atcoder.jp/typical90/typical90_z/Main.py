import sys
sys.setrecursionlimit(10**6)

n = int(input())

edge = [[] for _ in range(n + 1)]

for _ in range(n-1):
  a, b = map(int, input().split())
  edge[a].append(b)
  edge[b].append(a)

dist = [0] * (n+1)

def dfs(x, last=-1):
  for to in edge[x]:
    if to == last:
      continue
    dist[to] = dist[x] + 1
    dfs(to, x)

dfs(1)

nodes = [[], []]

for v in range(1, n+1):
  nodes[dist[v] % 2].append(v)

if len(nodes[0]) > len(nodes[1]):
  print(*nodes[0][:n//2])
else:
  print(*nodes[1][:n//2])