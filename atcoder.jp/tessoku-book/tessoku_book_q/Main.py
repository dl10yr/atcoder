n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [ None ] * (n+1)
dp[1] = 0
dp[2] = a[0]
for i in range(3, n+1):
    dp[i] = min(dp[i-1] + a[i-2], dp[i-2] + b[i-3])

answer = []
place = n
while True:
    answer.append(place)
    if place == 1:
        break
    if dp[place-1] + a[place-2] == dp[place]:
        place -= 1
    else:
        place -= 2

answer.reverse()
print(len(answer))
print(' '.join([f'{a}' for a in answer]))