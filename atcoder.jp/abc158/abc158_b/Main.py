N, A, B = map(int, input().split())
an = N // (A+B) * A
rem = N % (A+B)
an += min(rem,A)
print(an)