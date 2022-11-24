import statistics
import math

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xs = []
ys = []

for i in range(n):
  xs.append(xy[i][0])
  ys.append(xy[i][1])

med_x = statistics.median(xs)
med_y = statistics.median(ys)
x1 = math.floor(med_x)
x2 = math.ceil(med_x)
y1 = math.floor(med_y)
y2 = math.ceil(med_y)

abs_x1 = 0
abs_x2 = 0
abs_y1 = 0
abs_y2 = 0

for i in range(n):
  abs_x1 += abs(xy[i][0] - x1)
  abs_x2 += abs(xy[i][0] - x1)
  abs_y1 += abs(xy[i][1] - y1)
  abs_y2 += abs(xy[i][1] - y2)

print(min(abs_x1, abs_x2) + min(abs_y1, abs_y2))