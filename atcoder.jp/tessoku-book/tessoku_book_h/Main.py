h, w = map(int, input().split())


x_list = []
for _ in range(h):
    x_list.append(list(map(int, input().split())))
q = int(input())
q_list = []
for _ in range(q):
    q_list.append(list(map(int, input().split())))

sum_list = [[0] * (w + 1) for i in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        sum_list[i][j] = sum_list[i][j - 1] + x_list[i - 1][j - 1]
        
for j in range(1, w + 1):
    for i in range(1, h + 1):
        sum_list[i][j] = sum_list[i-1][j] + sum_list[i][j]

for i in range(q):
    a = q_list[i][0]
    b = q_list[i][1]
    c = q_list[i][2]
    d = q_list[i][3]

    ans = sum_list[c][d] - sum_list[a - 1][d] - sum_list[c][b - 1] + sum_list[a - 1][b - 1]
    print(ans)


