n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if n == 2:
    print(a[0])
elif n == 3:
    print(min(a[0] + a[1], b[0]))
elif n == 4:
    tmp = min(a[0] + a[1], b[0])
    print(min(tmp + a[4-2], a[0] + b[4-3]))
else:
    t = [ 0 ] * (n + 1)
    t[3] = min(a[0] + a[1], b[0])
    t[4] = min(t[3] + a[4-2], a[0] + b[4-3])

    for i in range(5, n+1):
        t[i] = min(t[i-1] + a[i-2], t[i-2] + b[i-3])
    print(t[n])
