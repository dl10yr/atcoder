n = int(input())
a = list(map(int, input().split()))

d = int(input())
l = [ None ] * d
r = [ None ] * d
for i in range(d):
    l[i], r[i] = map(int, input().split())

p = [ None ] * n
p[0] = a[0]
for i in range(1, n):
    p[i] = max(p[i - 1], a[i])
  
q = [ None ] * n
q[n - 1] = a[n - 1]
for i in reversed(range(0, n-1)):
    q[i] = max(q[i + 1], a[i])

for d in range(d):
    print(max(p[(l[d]-1) - 1], q[(r[d]+1) - 1]))