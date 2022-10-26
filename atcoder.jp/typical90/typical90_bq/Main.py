import math
import itertools

n, k = map(int, input().split())
## ans = k * (k-1) * (k-2)**(n-2)
if n == 1:
  print(k)
elif n == 2:
  print(k * (k-1))
else:
  base2 = ''
  tmp = n - 2
  while tmp > 0:
    amari = tmp % 2
    tmp = tmp // 2
    base2 = str(amari) + base2

  len_base2 = len(base2)
  tmp = 1
  for i in range(len_base2):
    if i == 0:
      pow2_amari = (pow(k - 2, pow(2, i))) % (pow(10, 9) + 7)
    else:
      pow2_amari = (pow2_amari * pow2_amari) % (pow(10, 9) + 7)

    if int(base2[len_base2 - 1 - i]) == 0:
      continue
    tmp = (tmp * pow2_amari) % (pow(10, 9) + 7)
  ans = (k * (k-1) * tmp) % (pow(10, 9) + 7)
  print(ans)