n = int(input())
a, b, c = map(int, input().split())
ans = pow(10, 18)
for i in range(10000):
    if a * i > n:
        break
    for j in range(10000-i):
        if a * i + b * j > n:
            break
        if (n - (a * i + b * j )) % c == 0:
            k = (n - (a * i + b * j )) / c
            ans = min(ans, i+j+k)

print(int(ans))