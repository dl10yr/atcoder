n, k = map(int, input().split())
checks = [False for _ in range(100000)]
num_list = []
while checks[n] == False:
  checks[n] = True
  num_list.append(n)
  n = n + sum(map(int, list(str(n))))
  n = n % 100000

interval = len(num_list) - num_list.index(n)
if k < len(num_list):
  ans = num_list[k]
else:
  k = k - len(num_list)
  if k >= interval:
    k = k % interval
  ans = num_list[num_list.index(n) + k]

print(ans)