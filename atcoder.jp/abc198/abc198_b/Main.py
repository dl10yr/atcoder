str_n = input()
int_n = int(str_n)
count = 0

if int_n == 0:
    print('Yes')
else:
    while(count == 0):
        if int_n % 10 == 0:
            int_n = int_n / 10
        else:
            count += 1

    str_n = str(int(int_n))

    if str_n == str_n[::-1]:
        print('Yes')
    else:
        print('No')