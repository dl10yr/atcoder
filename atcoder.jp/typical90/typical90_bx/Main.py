import bisect
n = int(input())
a = list(map(int, input().split()))
target_size = sum(a) * 0.1

a = [* a, * a]

a_sum_list = []
tmp = 0
for i in range(len(a)):
  tmp += a[i]
  a_sum_list.append(tmp)


l = n - 1
r = n
cnt = 0

for i in range(n):
 j = bisect.bisect_left(a_sum_list, target_size + a_sum_list[i])
 if a_sum_list[j] - a_sum_list[i] == target_size:
   exit(print("Yes"))

print('No')



