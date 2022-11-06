from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
distances = [-1 for _ in range(n)]

def get_distance(graph, start):
  distances = [-1 for _ in graph]
  q = deque()
  distances[start] = 0
  q.append(start)
  while q:
    p = q.popleft()
    for e in graph[p]:
      if distances[e] == -1:
        distances[e] = distances[p] + 1
        q.append(e)
  far = max(range(len(graph)), key=lambda i: distances[i])
  return distances[far], far

for i in range(n-1):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

_, p = get_distance(graph, 0)
dist, q = get_distance(graph, p)

print(dist + 1)


