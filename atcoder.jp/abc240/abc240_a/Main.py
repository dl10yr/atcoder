a, b= map(int, input().split())

ans ='No'
if a == 10:
    if b == 9 or b == 1:
        ans = 'Yes'
elif b == 10:
    if a == 9 or a == 1:
        ans = 'Yes'
if a == 1:
    if b == 10 or b == 2:
        ans = 'Yes'
elif b == 1:
    if a == 10 or a == 2:
        ans = 'Yes'
else:
    if abs(b-a) <= 1:
        ans = 'Yes'
print(ans)