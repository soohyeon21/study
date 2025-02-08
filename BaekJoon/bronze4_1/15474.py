# 15474

# 왜 이렇게 하면 '런타임 에러(NZEC)'가 발생할까?
# x = n//a if n%a==0 else n//a+1
# y = n//c if n%c==0 else n//c+1

import sys

n, a, b, c, d = map(int, sys.stdin.readline().split())

x = n//a
if (n%a != 0):
    x += 1
    
y = n//c
if (n%c != 0):
    y += 1

print(min(x*b, y*d))
