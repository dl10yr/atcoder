n = int(input())
cps = [list(map(int, input().split())) for cp in range(n)]
q = int(input())
lrs = [list(map(int, input().split())) for lr in range(q)]

## a組とb組とする
a_sums = []
a = 0
b_sums = []
b = 0
for cp in cps:
    if cp[0] == 1: 
        a += cp[1]
        a_sums.append(a)
        b_sums.append(b)
    else:
        b += cp[1]
        b_sums.append(b)
        a_sums.append(a)

for lr in lrs:
    start = 0 if lr[0] - 2 < 0 else a_sums[lr[0] - 2]
    ans_a = a_sums[lr[1]-1] - start
    start = 0 if lr[0] - 2 < 0 else b_sums[lr[0] - 2]
    ans_b = b_sums[lr[1]-1] - start  
    print(ans_a, ans_b)