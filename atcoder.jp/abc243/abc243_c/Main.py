import collections

n = int(input())
xy = [list(map(int, input().split())) for xy in range(n)]
y = list(map(lambda aa: aa[1], xy))
y = collections.Counter(y)    
y_c = list(y.items())
arieru_y = []
for i in range(len(y_c)):
    if y_c[i][1] >= 2:
        arieru_y.append(y_c[i][0])

s = input()
str_array = list(s)

arieru_xy = []
d = {}

for i in range(len(xy)):
    if xy[i][1] in arieru_y:
        prev = []
        if str(xy[i][1]) in d.keys():
            prev = d[str(xy[i][1])]
        else:
            prev = []
        prev.append(i)
        d[str(xy[i][1])] = prev
        
keys = list(d.keys())
ishantei = 0
for i in range(len(keys)):
    index = d[keys[i]]
    r_index = []
    l_index = []
    for m in range(len(index)):
        if str_array[index[m]] == 'R':
            r_index.append(xy[index[m]][0])
        else:
            l_index.append(xy[index[m]][0])
    if len(r_index) >= 1 and len(l_index) >= 1 and min(r_index) <= max(l_index):
        ishantei = 1
        break

if ishantei == 1:
    print('Yes')
elif ishantei == 0:
    print('No')