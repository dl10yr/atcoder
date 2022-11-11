n = int(input())
dots = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(n):
  lx, ly, rx, ry = map(int, input().split())
  for y in range(ly, ry):
    dots[y][lx] += 1
    dots[y][rx] -= 1

ans = [0 for _ in range(n+1)]
for dot in dots:
  t = 0
  for i in dot:
    t += i
    ans[t] += 1

for k in range(1, n + 1):
  print(ans[k])