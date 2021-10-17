# 2522

# rjust()도 사용 가능.

n = int(input())

for i in range(1,n + 1):
    print(" "*(n - i) + "*"*i)

for j in range(1, n):
    print(" "*j + "*"*(n - j))
