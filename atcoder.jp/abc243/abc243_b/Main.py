 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

one_index = []
r_a = []
r_b = []
cnt = 0
for i in range(n):
    if a[i] == b[i]:
        one_index.append(i)
    else:
        r_a.append(a[i])
        r_b.append(b[i])

for i in range(len(r_a)):
    if r_a[i] in r_b:
        cnt += 1
print(len(one_index))
print(cnt)
