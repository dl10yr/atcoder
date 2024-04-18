h, w = map(int, input().split())
c = [ [] ] * h
for i in range(h):
    c[i] = input()
dp = [ [ 0 ] * (w) for _ in range(h) ]

dp[0][0] = 1

for i in range(h):
    for j in range(w):
        upper = 0
        if i == 0 or c[i-1][j] == '#':
            upper = 0
        else:
            upper = dp[i-1][j]
        lefter = 0
        if j == 0 or c[i][j-1] == '#':
            lefter = 0
        else:
            lefter = dp[i][j-1]
        
        if i == 0 and j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = upper + lefter

print(dp[h-1][w-1])