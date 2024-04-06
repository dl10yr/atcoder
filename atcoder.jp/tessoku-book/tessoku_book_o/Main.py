n = int(input())
a = list(map(int, input().split()))

a_index_dict = {}

for i in range(n):
    old_indexs = a_index_dict.get(a[i], [])
    old_indexs.append(i)
    a_index_dict[a[i]] = old_indexs


a_sorted = sorted(a)

b_sorted = []
for i in range(n):
    if i == 0:
        b_sorted.append(1)
    else:
        if a_sorted[i] == a_sorted[i-1]:
            b_sorted.append(b_sorted[i-1])
        elif a_sorted[i] > a_sorted[i-1]:
            b_sorted.append(b_sorted[i - 1]+1)

b = [ None ] * n

for i in range(n):
    num_append = b_sorted[i]
    num_index = a_sorted[i]
    indexs = a_index_dict[num_index]
    b[indexs[0]] = num_append
    indexs.pop(0)
    a_index_dict[num_index] = indexs


print(' '.join([f'{b_num}' for b_num in b]))