n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[ None ] * (s + 1) for _ in range(n + 1)]

dp[0][0] = True
for i in range(1, s+1):
    dp[0][i] = False

for i in range(1, n+1):
    for j in range(0, s+1):
        if j < a[i-1]:
            ## a[i-1]は使わない
            if dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        if j >= a[i-1]:
            ## a[i-1]を使う
            if dp[i-1][j] == True or dp[i-1][j-a[i-1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[n][s] == True:
    print('Yes')
else:
    print('No') 