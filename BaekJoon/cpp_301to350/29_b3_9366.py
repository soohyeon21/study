# 9366

import sys

t = int(sys.stdin.readline())
for i in range(1, t+1):
    status = ""
    a, b, c = map(int, sys.stdin.readline().split())
    if (max(a, b, c) >= a+b+c-max(a, b, c)):
        status = "invalid!"
    elif ((a == b) and (b == c)):
        status = "equilateral"
    elif ((a == b) or (b == c) or (a == c)):
        status = "isosceles"
    else:
        status = "scalene"
    print(f"Case #{i}: {status}")
