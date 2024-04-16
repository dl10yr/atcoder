n, k = map(int, input().split())
a = list(map(int, input().split()))

## 2つの差がk以下になる組み合わせの数を考える
cnt = 0
for i in range(n):
    left = i
    right = n - 1
    while right > left:
        mid = (left + right) // 2
        if a[mid] - a[i] <= k:
            left = min(mid + 1, n -1)
        else:
            right = mid
    if a[left] - a[i] > k:
        left -= 1
    cnt += left - i
print(cnt)