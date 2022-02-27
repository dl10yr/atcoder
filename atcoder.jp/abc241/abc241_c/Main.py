n = int(input())
s = [input() for _ in range(n)]
 
dxs = [1, 1, 1, 0]
dys = [0, 1, -1, 1]
 
for i in range(n):
  for j in range(n):
    for d in range(4):
      dx = dxs[d]
      dy = dys[d]
      white_count = 0
      for k in range(6):
        nx = i + dx * k
        ny = j + dy * k
        if not (0 <= nx < n and 0 <= ny < n):
          white_count = 1000
          break
        if s[nx][ny] == '.':
          white_count += 1
      if (white_count <= 2):
        print('Yes')
        exit()
print('No')