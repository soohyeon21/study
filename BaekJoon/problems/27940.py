# 27940

# ti의 값이 얼마이든 1층은 항상 빗물이 누적되기 때문에, 1층만 살펴보아도 충분하다.

import sys

def IsCollapse(floor, n, m, k):
    for i in range(1, m+1):
        ti, ri = map(int, sys.stdin.readline().split())
        #for t in range(1, ti+1):
        floor[1] += ri
        if (floor[1] > k):
            return (i, 1)
    return False


n, m, k = map(int, sys.stdin.readline().split())
floor = [0 for x in range(n+1)]

collapse = IsCollapse(floor, n, m, k)

if (collapse):
    print(*collapse)
else:
    print(-1)
