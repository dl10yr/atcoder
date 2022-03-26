n = int(input())
a = list(map(int, input().split()))

a.sort()
a = list(set(a))
cnt = 0
iscontinue = True
while iscontinue:
    if cnt not in a:
        iscontinue = False
    else:
        cnt += 1
print(cnt)