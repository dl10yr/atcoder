N = int(input())
ab = [map(int, input().split()) for _ in range(N)]
a, b = [list(i) for i in zip(*ab)]


a_min = min(a)
b_min = min(b)

sorted_a = sorted(set(a))
sorted_b = sorted(set(b))
a_sec = 0
b_sec = 0
if len(sorted_a) >=2:
    a_sec=sorted_a[1]
if len(sorted_b) >=2:
    b_sec = sorted_b[1]


a_indexs = [i for i, v in enumerate(a) if v == min(a)]

b_indexs = [i for i, v in enumerate(b) if v == min(b)]

if len(sorted_a) == 1 and len(sorted_b) == 1:
    print(max([a_min, b_min]))
else:
    if a_indexs == b_indexs:
        if a_sec != 0 and b_sec != 0:
            print(min([a_min+b_min, max([a_min, b_sec]), max([a_sec, b_min])]))
        elif a_sec != 0 and b_sec == 0:
            print(min([a_min+b_min, max([a_sec, b_min])]))
        elif a_sec == 0 and b_sec != 0:
            print(min([a_min+b_min, max([a_min, b_sec])]))
    else:
        print(max([a_min, b_min]))