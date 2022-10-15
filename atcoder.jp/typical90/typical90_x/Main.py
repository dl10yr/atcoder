n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

minimum = 0

for i in range(n):
    minimum += abs(a[i] - b[i])
    
if minimum > k:
    print('No')

elif minimum % 2 ==  k % 2 :
    print('Yes')
    
else:
    print('No')