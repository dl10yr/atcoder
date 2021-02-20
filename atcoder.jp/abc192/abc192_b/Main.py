s = input()
isHantei = 0
for num in range(len(s)):
    if num % 2 == 0:
        if(s[num].islower()):
            isHantei += 0
        else:
            isHantei += 1
    else:
        if(s[num].islower()):
            isHantei += 1
        else:
            isHantei += 0
if isHantei != 0:
    print('No')
else:
    print('Yes')
