h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]
cnt = 0
for i in range(h-1):
  for j in range(w-1):
    diff = b[i][j] - a[i][j]
    cnt += abs(diff)
    a[i][j] += diff
    a[i+1][j] += diff
    a[i][j+1] += diff
    a[i+1][j+1] += diff
if a[h-1][w-1] != b[h-1][w-1]:
  print('No')
else:
  print('Yes')
  print(cnt)

