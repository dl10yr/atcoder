n, k = map(int, input().split())

nums = str(n)

for i in range(k):
  len_n = len(nums)
  tmp = 0
  for j in range(len_n):
    tmp += int(nums[j]) * pow(8, len_n - j - 1)
  if tmp == 0:
    nums = '0'
    continue
  nums = ''
  while tmp > 0:
    amari = tmp % 9
    tmp = tmp // 9
    if amari == 8:
      amari = 5
    nums = str(amari) + nums

print(''.join(nums))