n, m= map(int, input().split())
a = list(map(int, input().split()))

c = list(map(int, input().split()))

b = [0 for _ in range(m+1)]

for i in range(m, -1, -1):
    b[i] = c[i+n] / a[n]
    for j in range(n):
        c[i+j] -= b[i] * a[j]

print(" ".join([str(int(i)) for i  in b]))