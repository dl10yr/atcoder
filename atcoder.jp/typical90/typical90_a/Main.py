def hantei(num: int):
  cnt = 0
  pre = 0
  for i in range(n):
    if a[i] - pre >= num and l - a[i] >= num:
      cnt += 1
      pre = a[i]
  if cnt >= k:
    return True
  return False


n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

left = -1
right = l + 1

while right - left > 1:
  mid = left + (right - left) // 2
  if hantei(mid) == False:
    right = mid
  else:
    left = mid

print(left)