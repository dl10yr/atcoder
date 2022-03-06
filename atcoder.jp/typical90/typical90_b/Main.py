n = int(input())

items = []

for bit in range(2**n):
    cnt = 0
    target = ""
    for i in range(n):
        if (bit >> i) & 1:
            target =  target + "("
            cnt += 1
        else:
            target =  target + ")"
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        items.append(target)

items.sort()
for i in range(len(items)):
    print(items[i])