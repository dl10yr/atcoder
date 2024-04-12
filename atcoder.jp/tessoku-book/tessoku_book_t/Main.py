s = input()
t = input()
n = len(s)
l = len(t)

dp = [ [0] * (l + 1) for _ in range(n + 1) ]
dp[0][0] = 0
for i in range(n):
    for j in range(l):
        if s[i] == t[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n - 1][l - 1])