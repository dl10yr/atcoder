N, W = map(int, input().split())
w = [ None ] * (N + 1)
v = [ None ] * (N + 1)
for i in range(1, N + 1):
    w_i, v_i = map(int, input().split())
    w[i] = w_i
    v[i] = v_i

dp = [ [0] * (W + 1) for i in range(N + 1) ]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(0, W + 1):
        if j < w[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
print(dp[N][W])