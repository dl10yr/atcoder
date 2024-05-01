n, x, y = map(int, input().split())
a = list(map(int, input().split()))

grundy = [ None ] * 100001
for i in range(100001):
    transit = [False, False, False]
    if i >= x:
        transit[grundy[i-x]] = True
    if i >= y:
        transit[grundy[i-y]] = True
    
    if transit[0] == False:
        grundy[i] = 0
    elif transit[1] == False:
        grundy[i] = 1
    else:
        grundy[i] = 2

xor_sum = 0
for i in range(n):
    xor_sum = (xor_sum ^ grundy[a[i]])

if xor_sum >= 1:
    print('First')
else:
    print('Second')
	
          