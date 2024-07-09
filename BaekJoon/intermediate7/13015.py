# 13015

# 오른쪽 끝에 " "이 있으면 안된다.

import sys

n = int(sys.stdin.readline())

stars = ["*"*n + " "*(n*2-3) + "*"*n]
for i in range(1, n-1):
    left = " "*i + "*" + " "*(n-2) + "*" + " "*(n-2-i)
    line = left + " " + left[::-1]
    stars.append(line)
    
for one in stars:
    print(one.rstrip())

cleft = " "*(n-1) + "*" + " "*(n-2)
print(cleft + "*" + cleft[::-1].rstrip())

for one in reversed(stars):
    print(one.rstrip())
