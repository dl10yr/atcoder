h, w, n = map(int, input().split())

a = [ None ] * n
b = [ None ] * n
c = [ None ] * n
d = [ None ] * n

for t in range(n):
	a[t], b[t], c[t], d[t] = map(int, input().split())

x = [ [0] * (w + 2) for i in range(h + 2) ]
z = [ [0] * (w + 2) for i in range(h + 2) ]

for t in range(n):
    x[a[t]][b[t]] += 1
    x[a[t]][d[t]+1] -= 1
    x[c[t]+1][b[t]] -= 1
    x[c[t]+1][d[t]+1] += 1

for i in range(1, h+1):
    for j in range(1, w+1):
        z[i][j] = z[i][j-1] + x[i][j]

for j in range(1, w+1):
    for i in range(1, h+1):
        z[i][j] = z[i-1][j] + z[i][j]

for i in range(1, h+1):
    for j in range(1, w+1):
        if j >= 2:
            print(" ", end="")
        print(z[i][j], end="")
    print("")



