n, x = map(int, input().split())
a_list = list(map(int, input().split()))
is_yes = False
for a in a_list:
    if a == x:
        is_yes = True
        break

if is_yes == True:
    print('Yes')
else:
    print('No')