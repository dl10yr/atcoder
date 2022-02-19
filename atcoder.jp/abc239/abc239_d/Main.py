a, b, c, d= map(int, input().split())
sosu = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]

winners = []

min_sum = a+c
max_sum = b+d

targets = list(filter(lambda x: x >= min_sum and x <= max_sum, sosu))

for m in range(a, b+1):
    winner = 'Takahashi'
    for target in targets:
        aoki_target = target - m
        if aoki_target >= c and aoki_target <= d:
            winner = 'Aoki'
    winners.append(winner)

takahashis = list(filter(lambda x: x== 'Takahashi', winners))
if len(takahashis) >= 1:
    print('Takahashi')
else:
    print('Aoki')