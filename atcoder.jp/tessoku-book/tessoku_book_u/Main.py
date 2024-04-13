n = int(input())
p = [ None ] * (n + 1)
a = [ None ] * (n + 1)
for i in range(1, n + 1):
    p[i], a[i] = map(int, input().split())

dp = [ [ None ] * (n + 1) for _ in range(n + 1) ]
dp[1][n] = 0

## lenはl-r
for len in reversed(range(0, n - 1)):
    for l in range(1, n - len + 1):
        r = l + len
        
        ## l-1番目のブロックを取り除くときのスコア
        score_l_minus_1 = 0
        if l >= 2 and l <= p[l-1] and p[l-1] <= r:
            score_l_minus_1 = a[l-1]
        
        ## r+1番目のブロックを取り除くときのスコア
        score_r_plus_1 = 0
        if r <= n-1 and l <= p[r+1] and p[r+1] <= r:
            score_r_plus_1 = a[r+1]
        
        # dp[l][r]
        if l == 1:
            dp[l][r] = dp[l][r+1] + score_r_plus_1
        elif r == n:
            dp[l][r] = dp[l-1][r] + score_l_minus_1
        else:
            dp[l][r] = max(dp[l-1][r] + score_l_minus_1, dp[l][r+1] + score_r_plus_1)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dp[i][i])
print(ans)
