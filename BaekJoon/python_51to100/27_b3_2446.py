# 2446

n = int(input())

for i in range(n-1):
    print(" "*i + "*"*((n-i)*2 - 1))

for j in range(1, n+1):
    print(" "*(n-j) + "*"*(j*2 - 1))
