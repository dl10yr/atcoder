n, x = map(int, input().split())
l = [list(map(int, input().split())) for l in range(n)]
sums = l[0]
is_break = False
for i in range(1, n):
    local_sums = []
    for s in sums:
        local_sums.append(s+l[i][0])
        local_sums.append(s+l[i][1])
    sums = list(set(local_sums))
    if i <= n-2 and min(sums) >= x:
        is_break = True
        break
if x in sums and is_break == False:
    print('Yes')
else:
    print('No')