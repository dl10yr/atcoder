import math
n = int(input())
x0, y0 = map(int, input().split())
a, b = map(int, input().split())
c = (x0 + a) * 0.5
d = (y0 + b) * 0.5
theta = (math.radians(180 * (n-2)/n))

e = a - c
f = b - d

xx = math.cos(theta) * e + math.sin(theta) * f + c
yy = -1 * math.sin(theta) * e + math.cos(theta) * f + d
print(xx, yy)