n = int(input())

ans = 0
for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    if a == '+':
        ans += b
    elif a == '-':
        ans -= b
    elif a == '*':
        ans = ans * b

    ans = ans % (10000)
    print(ans)