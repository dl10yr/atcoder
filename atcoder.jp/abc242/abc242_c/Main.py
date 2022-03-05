m = 998244353
n = int(input())

dp = [[0 for _ in range(11)] for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(1, 10):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % m

print(sum(dp[n]) % m)