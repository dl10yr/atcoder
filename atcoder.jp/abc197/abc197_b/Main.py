h, w, x, y = map(int, input().split())
l = [input() for l in range(h)]
l_i = l[x-1]
l_j = ''
for i in range(len(l)):
    l_j += l[i][y-1]
count = 0
for i in reversed(range(0, y)):
    if l_i[i] == '#':
        break
    else:
        count += 1

for i in range(y, len(l_i)):
    if l_i[i] == '#':
        break
    else:
        count += 1

for i in reversed(range(0, x)):
    if l_j[i] == '#':
        break
    else:
        count += 1

for i in range(x, len(l_j)):
    if l_j[i] == '#':
        break
    else:
        count += 1
if count != 0:
    count -= 1
print(count)