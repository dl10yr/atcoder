def binary_search(a, target):
    left = -1
    right = len(a)
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid
        else:
            right = mid
    if a[left] == target:
        return left
    elif a[left + 1] == target:
        return left + 1
    else:
        return None
    
n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = binary_search(a, x)
print(ans + 1)
