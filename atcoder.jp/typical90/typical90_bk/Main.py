h, w = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(h)]
ans = 0
for bit in range(1, 1 << h):
  selected_rows = []
  for i in range(h):
    if (bit & (1 << i)):
      selected_rows.append(i)
  cnt = {}
  for j in range(w):
    tmp = p[selected_rows[0]][j]
    if not all(p[row][j] == tmp for row in selected_rows):
      continue
    if tmp not in cnt:
      cnt[tmp] = 1
    else:
      cnt[tmp] += 1
  selected_col_max = 0
  for v in cnt.values():
    selected_col_max = max(selected_col_max, v)
  ans = max(ans, len(selected_rows) * selected_col_max)
print(ans)