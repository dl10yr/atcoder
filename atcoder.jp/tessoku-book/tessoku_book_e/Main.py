n, k = map(int, input().split())

count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        l = k - (i + j)
        if l >= 1 and l <= n:
           count += 1
        if l <= 0:
            break


print(count)