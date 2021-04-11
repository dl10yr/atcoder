import math


r, x, y= map(int, input().split())
kyori = math.sqrt(x**2 + y**2)

if kyori == 0:
    print('2')
else:
    if kyori % r == 0:
        print(int(kyori/r))
    else:
        waru = int(math.floor(kyori/r))
        if waru < 1:
            print('2')
        else:
            print(waru+1)