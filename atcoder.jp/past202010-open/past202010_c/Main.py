n, k = map(int, input().split())
rows = [input() for _ in range(n)]
rows.insert(0, '.'.join(['.' for _ in range(k)]))
rows.append('.'.join(['.' for _ in range(k)]))
new_rows = ['.' + _ + '.' for _ in rows]

for i in range(1, n+1):
    ans_row = ''
    for j in range(1, k+1):
        ans_str = new_rows[i][j] + new_rows[i-1][j] + new_rows[i+1][j] + new_rows[i][j-1] + new_rows[i][j+1] + new_rows[i-1][j-1] + new_rows[i-1][j+1] + new_rows[i+1][j-1] + new_rows[i+1][j+1]
        ans_row += str(ans_str.count('#'))
    print(ans_row) 