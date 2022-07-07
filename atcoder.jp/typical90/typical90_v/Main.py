import math

a, b, c = map(int, input().split())
ab_gcd = math.gcd(a, b)
gcd = math.gcd(ab_gcd, c)

a_kaisu = ( a // gcd ) -1
b_kaisu = ( b // gcd ) -1
c_kaisu = ( c // gcd ) -1
print(int(a_kaisu  + b_kaisu + c_kaisu))