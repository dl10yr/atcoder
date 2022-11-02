l, r = map(int, input().split())

def count(num):
  i = 1
  cnt = 0
  while True:
    first = pow(10, i - 1) - 1
    last = min(num, pow(10, i) - 1)
    cnt += ((last * (last + 1) - first * (first + 1)) // 2) * i
    if num <= pow(10, i) - 1:
      return cnt
    i += 1


print((count(r) - count(l - 1)) % (10 ** 9 + 7))
