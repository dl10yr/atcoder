S = list(input())
N = len(S)

def palindrome(string): return 0 if string==string[::-1] else 1

aaa = "".join(S)
tmp = int((N-1)/2-1)
bbb = "".join(S[0:tmp+1])
tmp = int((N+3)/2-1)
ccc = "".join(S[tmp:N])

sum = palindrome(aaa)+palindrome(bbb)+palindrome(ccc)


if sum ==0:
  print("Yes")
else:
  print("No")