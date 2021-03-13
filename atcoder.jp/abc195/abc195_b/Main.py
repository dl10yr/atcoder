import math

a,b,w = map(int, input().split())

isHantei = 1000 * w / a
max_number = math.floor(1000 * w / a)
min_number = math.ceil(1000 * w / b)

if max_number == min_number:
    print(max_number, max_number)
elif min_number > max_number:
    print('UNSATISFIABLE')
else:
    print(min_number, max_number)