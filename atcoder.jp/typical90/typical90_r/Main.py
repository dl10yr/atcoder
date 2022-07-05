import math

t = int(input())
l,x,y = map(int, input().split())
q = int(input())
es = [int(input()) for i in range(q)]
for e in es:
    yy = -1 * (l/2) * math.sin(2 * math.pi * e / t)
    z = (l/2) * (1- math.cos(2 * math.pi * e / t))
    tan = z / (math.sqrt(x**2 + (y-yy) **2))
    print(math.degrees(math.atan(tan)))