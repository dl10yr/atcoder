n, q = map(int, input().split())
a = list(map(int, input().split()))

t_cnt = 0
for i in range(q):
  t, x, y = map(int, input().split())
  diff = t_cnt % n

  convert_x = x - diff - 1 if x - diff - 1 >= 0 else x - diff - 1 + n
  convert_y = y - diff - 1 if y - diff - 1 >= 0 else y - diff - 1 + n
  if t == 1:
    tmp = a[convert_x]
    a[convert_x] = a[convert_y]
    a[convert_y] = tmp
  if t == 2:
    t_cnt += 1
  if t == 3:
    print(a[convert_x])