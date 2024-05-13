n, m, b = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

c_sum = sum(c)
a_sum = sum(a)

print(c_sum * n + a_sum * m + b * (m * n))