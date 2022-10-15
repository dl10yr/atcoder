import itertools

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
m = int(input())

funaka = [[False for i in range(n)] for j in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    funaka[x-1][y-1] = True
    funaka[y-1][x-1]  = True

    
ans = 10 ** 18
for p in itertools.permutations(range(n)):
    tmp = a[p[0]][0]
    is_nakayoshi = True
    for i in range(n-1):
        tmp += a[p[i+1]][i+1]
        if funaka[p[i]][p[i+1]] == True:
            is_nakayoshi = False
            break
    if is_nakayoshi:
        ans = min(ans, tmp)

if ans == 10 ** 18:
    print(-1)
else:
    print(ans)