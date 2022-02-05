n = int(input())
at = list(map(int, input().split()))

last_pos = [0]
current_sum = 0

for i in range(n):
    current_sum += at[i]
    push_value = current_sum % 360
    last_pos.append(push_value)

last_pos.sort()

diffs = []
for i in range(n-1):
    diffs.append(last_pos[i+1] - last_pos[i])
diffs.append(360-last_pos[-1])
print(max(diffs))
