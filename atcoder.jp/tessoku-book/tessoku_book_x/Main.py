import bisect


n = int(input())

a = list(map(int, input().split()))

length = 0
l = []
dp = [ None ] * n

for i in range(n):
    pos = bisect.bisect_left(l, a[i])
    dp[i] = pos

    if dp[i] >= length:
        l.append(a[i])
        length += 1
    else:
        l[dp[i]] = a[i]
   
print(length)