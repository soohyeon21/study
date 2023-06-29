# 1673

import sys

while (1):
    try:
        n, k = map(int, sys.stdin.readline().split())
    except: # EOFError, ValueError
        break

    cnt = n
    coup = n
    while (coup >= k):
        cnt += coup//k
        coup = coup//k + coup%k

    print(cnt)
