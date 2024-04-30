n = int(input())
a = list(map(int, input().split()))

xor_sum = a[0]

for i in range(1,n):
    xor_sum = xor_sum ^ a[i]

if xor_sum >= 1:
    print('First')
else:
    print('Second')