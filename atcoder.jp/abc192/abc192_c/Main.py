def calcF(num):
    numList = list(num)
    numIncList = sorted(numList)
    numDecList = sorted(numList, reverse=True)
    
    inc_number = 0
    dec_number = 0
    for i in range(len(numIncList)):
        inc_number += int(numIncList[i]) * 10**(i)
    for m in range(len(numDecList)):
        dec_number += int(numDecList[m]) * 10**(m)
    return inc_number - dec_number
    


# write codes
inputlist = input().split(' ')
n = inputlist[0]
k = int(inputlist[1])

for i in range(k):
    n = calcF(str(n))
print(n)