# 14542

# n=1인 경우 생각

import sys

idx = 1
while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    isum = int(sys.stdin.readline())
    if (n > 1):
        for _ in range(n-2):
            tmp = list(map(int, sys.stdin.readline().split()))
            isum += tmp[0]+tmp[-1]
        isum += sum(list(map(int, sys.stdin.readline().split())))

    print(f"Case #{idx}:{isum}")
    idx += 1
