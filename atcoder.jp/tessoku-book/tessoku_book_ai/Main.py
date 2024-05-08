n = int(input())
a = list(map(int, input().split()))

dp = [ [ None ] * (n+1) for i in range(n+1) ]

for j in range(1, n+1):
    ## n段目
    dp[n][j] = a[j-1]

for i in reversed(range(1, n)):
    for j in range(1, i+1):
        if i % 2 == 1:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])

print(dp[1][1])