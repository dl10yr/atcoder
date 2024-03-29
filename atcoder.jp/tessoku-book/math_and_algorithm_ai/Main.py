n, q = map(int, input().split())

a_list = list(map(int, input().split()))

l_list = []
r_list = []

for _ in range(q):
    l, r = map(int, input().split())
    l_list.append(l)
    r_list.append(r)

visitor_count_dict = {}

for i in range(n):
    if i == 0:
        visitor_count_dict[i] = a_list[i]
    else:
        visitor_count_dict[i] = visitor_count_dict[i - 1] + a_list[i]
    
for i in range(q):
    if l_list[i] - 2 < 0:
        num_of_visitors = visitor_count_dict[r_list[i] - 1]
    else:
        num_of_visitors = visitor_count_dict[r_list[i] - 1] - visitor_count_dict[l_list[i] - 2]

    print(num_of_visitors)