# 5724

# 1부터 n까지의 제곱의 합 공식

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    ssum = n*(n+1)*(2*n+1)//6
    print(ssum)
