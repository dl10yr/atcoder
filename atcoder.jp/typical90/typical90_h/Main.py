n = int(input())
s = input()
t = 'atcoder'
mod = pow(10, 9) + 7

dp = [[0 for _ in range(n+1)] for _ in range(len(t)+1)]

for k in range(n+1):
  dp[0][k] = 1

for i in range(n):
  for j in range(len(t)):
    if s[i] == t[j]:
      dp[j+1][i+1] = (dp[j][i+1] + dp[j+1][i]) % mod
    else:
      dp[j+1][i+1] = dp[j+1][i]

print(dp[len(t)][n])