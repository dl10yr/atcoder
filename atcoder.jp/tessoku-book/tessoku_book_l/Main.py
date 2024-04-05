def check(x, n, k, a):
    sum = 0
    for i in range(n):
        sum += x // a[i]
    if sum >= k:
        return True
    else:
        return False
    
    
n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 1
right = 10 ** 9
while left < right:
    mid = (left + right) // 2
    result = check(mid, n, k, a)
    if result == True:
        right = mid
    else:
        left = mid + 1

print(left)