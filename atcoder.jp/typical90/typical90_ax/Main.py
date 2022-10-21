import math
import itertools


n, l = map(int, input().split())
dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
  if i - l >= 0:
    dp[i] = dp[i-1] + dp[i-l]
  else:
    dp[i] = dp[i-1]
print(dp[n] % (pow(10, 9) + 7))
