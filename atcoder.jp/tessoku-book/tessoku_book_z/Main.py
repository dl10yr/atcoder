n = int(input())
for i in range(n):
    target = int(input())
    print_string = 'Yes'
    upper = int(target ** 0.5) + 1
    for j in range(2, upper):
        if target % j == 0:
            print_string = 'No'
            break
        else:
            continue
    print(print_string)