import itertools
L, R = map(int,input().split())
a = len(list(itertools.combinations(range(L), 2))) + len(list(itertools.combinations(range(R), 2)))
print(a)