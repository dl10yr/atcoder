n, m = map(int, input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
isbreak = False
for i in range(len(b)):
    try:
        a.remove(b[i])
    except:
        print('No')
        isbreak = True
        break
if isbreak == False:
    print('Yes')