N = int(input())
lis = list(map(int, input().split()))
sum_list = sum(lis)
sum_sq_list = sum_list * sum_list
sq_lis = [i ** 2 for i in lis]
sum_sq_list2 = sum(sq_lis)
minuses = sum_sq_list - sum_sq_list2

kaisu = N * (N-1) * 0.5 - (N-1) *(N-2) * 0.5
print(int(kaisu * sum_sq_list2 - minuses))