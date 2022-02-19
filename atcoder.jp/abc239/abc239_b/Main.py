x = input()
int_x = int(x)
if int_x == 0:
    print('0')
elif -10 < int_x  and int_x < 0:
    print('-1')
elif 0 < int_x  and int_x < 10:
    print('0')
elif int_x >= 10:
    tmp = x[:-1]
    print(tmp)
elif int_x <= -10:
    tmp = x[:-1]
    last_str = x[-1]
    if last_str == '0':
        print(tmp)
    else:
        print(int(tmp) - 1)