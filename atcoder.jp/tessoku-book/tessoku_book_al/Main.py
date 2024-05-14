
d, n = map(int, input().split())
l_list = []
r_list = []
h_list = []
if n == 0:
    print(24 * d)
    exit()
    
for i in range(n):
    l, r, h = map(int, input().split())
    l_list.append(l)
    r_list.append(r)
    h_list.append(h)

hour_list = [0] * (d)
for i in range(n):
    l = l_list[i]
    r = r_list[i]
    h = h_list[i]
    for j in range(l, r  + 1):
        prev = hour_list[j-1]
        if prev == 0:
            hour_list[j-1] = h
            continue
        if h < prev:
            hour_list[j-1] = h

print(sum(hour_list))
          