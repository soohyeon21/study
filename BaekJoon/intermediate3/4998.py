# 4998

# try-except EOFError

import sys

while (1):
    ex = sys.stdin.readline().rstrip()
    if (ex == ""):
        break

    n, b, m = map(float, ex.split())
    year = 0
    while (n < m):
        n *= (1+0.01*b)
        year += 1

    print(year)
