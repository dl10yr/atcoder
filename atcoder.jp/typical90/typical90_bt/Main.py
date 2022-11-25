import math
import itertools


h, w = map(int, input().split())
c = [input().replace('\r', '') for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
use = [[0 for _ in range(w)] for _ in range(h)]
ans = -1

def dfs(sx, sy, px, py):
  if sx == px and sy == py and use[sy][sx] == 1: return 0
  use[py][px] = 1

  ret = -100
  for i in range(4):
    nx = px + dx[i]
    ny = py + dy[i]
    if nx < 0 or ny < 0 or nx >= w or ny >= h or c[ny][nx] == '#': continue
    if (sx != nx or sy != ny) and use[ny][nx] == 1: continue
    tmp = dfs(sx, sy, nx, ny)
    ret = max(ret, tmp + 1)

  use[py][px] = 0
  return ret


for i in range(w):
  for j in range(h):
    ans = max(ans, dfs(i, j, i, j))
 
if ans <= 2:
  ans = -1

print(ans)
