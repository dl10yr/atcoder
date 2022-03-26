n, k= map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [False for _ in range(n)]
ep = [False for _ in range(n)]
dp[0] = True
ep[0] = True

for i in range(n-1):
    if dp[i]:
        if abs(a[i+1] - a[i]) <= k:
            dp[i+1] = True
        if abs(b[i+1] - a[i]) <= k:
            ep[i+1] = True
    if ep[i]:
        if abs(a[i+1] - b[i]) <= k:
            dp[i+1] = True
        if abs(b[i+1] - b[i]) <= k:
            ep[i+1] = True
if dp[n-1] or ep[n-1]:
    print('Yes')
else:
    print('No')