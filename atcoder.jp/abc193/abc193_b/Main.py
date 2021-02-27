def nandai(a, x):
    b = a - 0.5
    if b < 0:
        return x
    else:
        return x - b


# write codes
N = int(input())
a = [0] * N
p = [0] * N
x = [0] * N
for i in range(N):
    a[i], p[i], x[i] = map(int, input().split())

kakaku = []

for i in range(N):
    nokori = nandai(a[i], x[i])
    if nokori >= 1:
        kakaku.append(p[i])
if len(kakaku) == 0:
    print(-1)
else:
    print(min(kakaku))