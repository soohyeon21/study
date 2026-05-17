# 홀짝 구분하기

import sys

n = int(sys.stdin.readline())

if (n % 2 == 0):
    print(f"{n} is even")
else:
    print(f"{n} is odd")
