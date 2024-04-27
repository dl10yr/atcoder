# a の b 乗を m で割った余りを返す関数
def Power(a, b, m):
	p = a
	Answer = 1
	for i in range(30):
		wari = 2 ** i
		if (b // wari) % 2 == 1:
			Answer = (Answer * p) % m # a の 2^i 乗が掛けられるとき
		p = (p * p) % m
	return Answer

# a÷b を m で割った余りを返す関数
def Division(a, b, m):
	return (a * Power(b, m - 2, m)) % m

n, r = map(int, input().split())

m = 1000000007


a = 1
for i in range(1, n+1):
    a = (a * i) % m

b = 1
for i in range(1, r+1):
    b = (b * i) % m
for i in range(1, n-r+1):
    b = (b * i) % m

print(Division(a, b, m))

          