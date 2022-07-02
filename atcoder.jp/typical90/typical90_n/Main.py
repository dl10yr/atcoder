n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
min_inconvinience = 0
for i in range(n):
    min_inconvinience += abs(a[i] - b[i])

print(min_inconvinience)