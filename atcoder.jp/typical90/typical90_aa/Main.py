n = int(input())
names = [input() for i in range(n)]

d = {}
for i in range(n):
    if d.get(names[i]) == None:
        d.setdefault(names[i], True)
        print( i + 1)