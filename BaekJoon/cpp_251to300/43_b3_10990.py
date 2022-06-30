# 10990

# 1/rest로 분리해서 생각해도 되더라.

import sys

n = int(sys.stdin.readline())
k = 0

for i in range(n-1, -1, -1):
    star = " "*i + "*"
    star2 = ""
    if (k != 0):
        star2 = " "*(2*k - 1) + "*"
    star += star2
    k += 1
    print(star)
