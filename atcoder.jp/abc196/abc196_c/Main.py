n = int(input())
count = 0
if n >= 1 and n < 10:
    count = 0
elif n>=10 and n < 100:
    count = 0
    n_str = str(n)
    n_0 = int(n_str[0])
    count += n_0
    if n < n_0*10 + n_0:
        count -= 1
elif n>=100 and n < 1000:
    count = 9
elif n>=10**3 and n < 10**4:
    count = 9
    n_str = str(n)
    n_1 = int(n_str[0])
    n_0 = int(n_str[1])
    n_count = n_1 * 10**1 + n_0
    count = count + n_count - 9
    if n < n_count * 100 + n_count:
        count -= 1
elif n>=10**4 and n < 10**5:
    count = 99
elif n>=10**5 and n < 10**6:
    count = 99
    n_str = str(n)
    n_2 = int(n_str[0])
    n_1 = int(n_str[1])
    n_0 = int(n_str[2])
    n_count = n_2 * 10**2 + n_1 * 10 + n_0
    count = count + n_count - 99
    if n < n_count * 1000 + n_count:
        count -= 1
elif n>=10**6 and n < 10**7:
    count = 999
elif n>=10**7 and n < 10**8:
    count = 999
    n_str = str(n)
    n_3 = int(n_str[0])
    n_2 = int(n_str[1])
    n_1 = int(n_str[2])
    n_0 = int(n_str[3])
    n_count = n_3 * 10**3 + n_2 * 10 ** 2 + n_1 * 10 + n_0
    count = count + n_count - 999
    if n < n_count * 10000 + n_count:
        count -= 1
elif n>=10**8 and n < 10**9:
    count = 9999
elif n>=10**9 and n < 10**10:
    count = 9999
    n_str = str(n)
    n_4 = int(n_str[0])
    n_3 = int(n_str[1])
    n_2 = int(n_str[2])
    n_1 = int(n_str[3])
    n_0 = int(n_str[4])
    n_count = n_4 * 10**4 + n_3 * 10**3 + n_2 * 10 ** 2 + n_1 * 10 + n_0
    count = count + n_count - 9999
    if n < n_count * 100000 + n_count:
        count -= 1
elif n>=10**10 and n < 10**11:
    count = 99999
elif n>=10**11 and n < 10**12:
    count = 99999
    n_str = str(n)
    n_5 = int(n_str[0])
    n_4 = int(n_str[1])
    n_3 = int(n_str[2])
    n_2 = int(n_str[3])
    n_1 = int(n_str[4])
    n_0 = int(n_str[5])
    n_count = n_5 * 10** 5 + n_4 * 10**4 + n_3 * 10**3 + n_2 * 10 ** 2 + n_1 * 10 + n_0
    count = count + n_count - 99999
    if n < n_count * 1000000 + n_count:
        count -= 1

print(count)