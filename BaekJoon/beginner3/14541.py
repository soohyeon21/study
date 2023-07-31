# 14541

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == -1):
        break

    data = [tuple(map(int, sys.stdin.readline().split())) for x in range(n)]
    dist = data[0][0]*data[0][1] + sum(data[i][0]*(data[i][1]-data[i-1][1]) for i in range(1, n))
    print(f"{dist} miles")
