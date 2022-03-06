 
h, w = map(int, input().split())

a =  [list(map(int, input().split())) for at in range(h)]
row_sum = []
col_sum = []

for i in range(h):
    row_sum.append(sum(a[i]))
for i in range(w):
    col = list(map(lambda x: x[i], a))
    col_sum.append(sum(col))

ans = []
for i in range(h):
    row_ans = []
    for j in range(w):
        row_ans.append(str(row_sum[i] + col_sum[j] - a[i][j]))
    ans.append(row_ans)

for i in range(h):
    print(' '.join(ans[i]))