d = int(input())
n = int(input())

l_list = []
r_list = []

for _ in range(n):
    l, r = map(int, input().split())
    l_list.append(l)
    r_list.append(r)

b = [0] * (d + 2)

for i in range(n):
    b[l_list[i]] += 1
    b[r_list[i] + 1] -= 1

ans = [ None ] * (d + 2)
ans[0] = 0
for i in range(1, d + 1):
    ans[i] = ans[i - 1] + b[i]
    
for i in range(1, d + 1):
    print(ans[i])