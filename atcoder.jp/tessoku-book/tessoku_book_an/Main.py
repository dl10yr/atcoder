n = int(input())
a = list(map(int, input().split()))

a_dict = {}

for i in range(n):
    a_dict[a[i]] = a_dict.get(a[i], 0) + 1

a_keys = a_dict.keys()
ans = 0
for a_key in a_keys:
    num_of_a_key = a_dict[a_key]
    if num_of_a_key < 3:
        continue
    else:
        ans += (num_of_a_key * (num_of_a_key - 1) * (num_of_a_key - 2)) // 6

print(ans)