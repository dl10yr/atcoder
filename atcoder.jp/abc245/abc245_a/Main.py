a, b, c, d= map(int, input().split())

takahashi = a * 3600 + b * 60
aoki = c * 3600 + d * 60 + 1
if takahashi < aoki:
    print('Takahashi')
else:
    print('Aoki')