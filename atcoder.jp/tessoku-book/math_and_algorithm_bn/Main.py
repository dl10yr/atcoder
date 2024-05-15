n = int(input())
a = []
for i in range(n):
    l, r = map(int, input().split())
    a.append((r, l))

a.sort()

currenttime = 0
ans = 0
for i in range(n):
    if currenttime <= a[i][1]:
        ans += 1
        currenttime = a[i][0]
print(ans)