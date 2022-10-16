def get_gcd(a, b):
  if b == 0:
    return a
  r = a % b
  return get_gcd(b, r)

a, b = map(int, input().split())

gcd = get_gcd(a, b)

r = a * b // gcd
if r > pow(10, 18):
  print('Large')
else: 
  print(int(r))