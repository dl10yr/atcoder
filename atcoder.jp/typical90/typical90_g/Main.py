n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

def search_def(a, target):
    left = -1
    right = n
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] == target:
            return 0
        elif a[middle] < target:
            left = middle
        else:
            right = middle
    can1 = 10**10
    can2 = 10**10
    if left >= 0:
        can1 = abs(a[left] - target)
    if left < n-1:
        can2 = abs(a[left+1]- target)
    return min([can1, can2])

a.sort()
for i in range(q):
    ans = search_def(a, b[i])
    print(ans)