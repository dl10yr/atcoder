x = input()
m = int(input())

def Base_n_to_10(X,N): # N進数のXを10進数に変換
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(N**(i-1))
    return out

d = 0
for i in range(len(x)): # dを求める
    d = max(d,int(x[i]))

n = d

if len(x) == 1:  # Xが一桁の場合はコーナーケース
    if int(x) <= m:
        ans = 1
    else:
        ans = 0
else: # 二分探索
    left = n
    right = m + 1
    while right - left > 1:
        mid = (left + right) // 2
        if Base_n_to_10(x,mid) > m:
            right = mid
        else:
            left = mid
    ans = left - n
print(ans)