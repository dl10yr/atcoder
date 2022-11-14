k = int(input())

if k % 9 != 0:
  print(0)
else:
  dp = [0 for _ in range(k+1)]
  dp[0] = 1
  for i in range(1, k+1):
    tmp = min(9, i)
    for j in range(1, tmp + 1):
      dp[i] += dp[i-j]
  print(dp[k] % (pow(10, 9) + 7))



