n, m, q = map(int,input().split())

WV = []
for i in range(n):
    array = list(map(int,input().split()))
    WV.append(array)
WV.sort(key=lambda x:x[1], reverse=True) # 価値Vの降順にソート

X = list(map(int,input().split()))

Q = []
for i in range(q):
    array = list(map(int,input().split()))
    Q.append(array)

# クエリ分だけループ
for i in range(q):  # i番目のクエリ
    ans = 0
    X_copy = X[:] # リストXをコピー
    del X_copy[Q[i][0]-1:Q[i][1]]   # LからRの箱を消去
    X_copy.sort()   # 箱の大きさを昇順でソート
    for wv in WV:   # 荷物のループ(Vが大きい順)
        for j in range(len(X_copy)):    #箱のループ(大きさが小さい順)
            if wv[0] <= X_copy[j]:  # 探索中の箱に荷物が入れば
                ans += wv[1]        # 価値Viを足して
                X_copy.pop(j)       # 荷物を入れた箱を消去
                break
    print(ans)