# 5691

import sys

while (1):
    a, b = map(int, sys.stdin.readline().split())
    if (a == 0 and b == 0):
        break

    # a가 평균&중앙값일 때
    c = 2*a - b

    print(c)
