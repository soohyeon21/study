# 4159

# 더슨 크릭(Dawson Creek)(0 mile)에는 충전소가 반드시 있지만,
# 델타 정션(Delta Junction)(1442 mile)에는 충전소가 있을 수도 있고, 없을 수도 있다.

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    station = [int(sys.stdin.readline()) for _ in range(n)]+[0, 1442]
    station.sort()
    dist = [station[i] - station[i-1] for i in range(1, n+2)]
    dist = dist[:-1]+[dist[-1]*2]

    state = True
    for d in dist:
        if (d > 200):
            state = False
            break

    if (not state):
        print("IM", end="")
    print("POSSIBLE")
