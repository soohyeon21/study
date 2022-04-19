# 10474

# denominator: 분모
# numerator: 분자

import sys

while (True):
    num, denom = map(int, sys.stdin.readline().split())
    if ((num == 0) and (denom == 0)):
        break

    print(num//denom, num%denom, "/", denom)
