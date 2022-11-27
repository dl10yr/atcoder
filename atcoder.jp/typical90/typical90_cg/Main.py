import math

k = int(input())
divs = []
for i in range(1, math.floor(k**0.5) + 1):
  if k % i != 0: continue
  divs.append(i)
  if i != k / i: divs.append(int(k / i))
ans = 0

for i in range(len(divs)):
  for j in range(i, len(divs)):
    a = divs[i]
    b = divs[j]
    c = 0
    if k / a < b: continue
    if k % (a * b) != 0: continue
    c = k / (divs[i] * divs[j])
    if b <= c: ans += 1

print(ans)