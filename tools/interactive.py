import sys
n = int(input())
lst = list(range(1, 2*n+2))
is_first = True
now_number = 1
while now_number != 0:
    if is_first == False:
        lst.remove(now_number)
    is_first = False
    
    print(lst[0], flush=True)
    lst.remove(lst[0])
    now_number = int(input())
sys.exit(10)