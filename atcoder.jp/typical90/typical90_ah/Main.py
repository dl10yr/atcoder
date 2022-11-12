n, k = map(int, input().split())
a = list(map(int, input().split()))

r, ans = 0, 0
cnt = 0
d = {}
for l in range(n):
  while r < n and cnt <= k:
    if not a[r] in d:
      d[a[r]] = 0
    if d[a[r]] == 0:
      if cnt == k:
        break
      cnt += 1
    d[a[r]] += 1
    r += 1
  ans = max(ans, r - l)
  d[a[l]] -= 1
  if d[a[l]] == 0:
    cnt -= 1

print(ans)