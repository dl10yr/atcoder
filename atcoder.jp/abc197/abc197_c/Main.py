def solve():
    from itertools import product

    N = int(input())
    A = [*map(int, input().split())]

    ans = float('INF')

    for _bit in product((True, False), repeat=N - 1):
        bit = list(_bit) + [True]  # A[N-1]の右に常に区切り棒があることにします
        score = 0  # 各区間のXOR
        cur = 0  # 現区間のOR
        for i in range(N):
            cur |= A[i]  # | -> or
            if bit[i]:
                # 区切り棒が来たら、今の区間は終わりです
                score ^= cur  # ^ -> xor
                cur = 0  # 区間のorを0にリセットします

        # N番目の区切り棒を追加しているので、最後の区間を特別に処理せずに済みます

        ans = min(ans, score)  # 最小値を更新します

    print(ans)


solve()