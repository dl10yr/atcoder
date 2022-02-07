def solve():
    a, s = map(int, input().split())
    t = s - 2 * a
    if t < 0:
        return False
    return t & a == 0

T = int(input())
for _ in range(T):
    print("Yes" if solve() else "No")