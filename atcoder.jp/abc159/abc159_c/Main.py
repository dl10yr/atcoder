import decimal
decimal.getcontext().prec = 20
S = decimal.Decimal(input()) 
s = S/3
print(decimal.Decimal(s**3))