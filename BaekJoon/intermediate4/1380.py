# 1380

import sys

tcase = 1
while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    names = [sys.stdin.readline().rstrip() for _ in range(n)]
    check = {i:0 for i in range(1, n+1)}
    for j in range(2*n-1):
        num, ab = sys.stdin.readline().split()
        check[int(num)] += 1

    for k, v in check.items():
        if (v != 2):
            print(tcase, names[k-1])
            break

    tcase += 1
