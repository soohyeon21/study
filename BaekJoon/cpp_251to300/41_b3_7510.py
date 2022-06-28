# 7510

import sys

n = int(sys.stdin.readline())
status = ""

for i in range(1, n+1):
    a, b, c = map(int, sys.stdin.readline().split())
    if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2)):
        status = "yes"
    else:
        status = "no"

    print(f"Scenario #{i}: \n{status}\n")
