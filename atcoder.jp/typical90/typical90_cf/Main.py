n = int(input())
s = input()

searched = []
tmp = [s[0], 1]

for i in range(1, n):
  if tmp[0] == s[i]:
    tmp = [tmp[0], tmp[1] + 1]
  else:
    searched.append(tmp)
    tmp = [s[i], 1]

if len(tmp) > 0:
  searched.append(tmp)

ret_cnt = 0
for i in range(len(searched)):
  ret_cnt += searched[i][1] * (searched[i][1] + 1) // 2

all = n * (n + 1) // 2
print(all - ret_cnt)

