def power(a, b, m):
    p = a
    answer = 1
    for i in range(30):
        wari = 2 ** i
        if (b // wari) % 2 == 1:
            answer = (answer * p) % m
        p = (p * p) % m
    return answer 

a, b = map(int, input().split())
print(power(a, b, 1000000007))