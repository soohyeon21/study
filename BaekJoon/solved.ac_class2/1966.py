# 1966

# if any(val < val2 for _, val2 in deque):
# any() # 하나라도 True가 있으면 True
# all() # 모두 True여야 True

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())
    prio = list(map(int, sys.stdin.readline().split()))
    docu = [i for i in range(1, n+1)]

    wanted = docu[m]

    th = 1
    while (len(docu) != 0):
        if (prio[0] >= max([0]+prio[1:])):
            if (docu[0] == wanted):
                print(th)
                break
            docu.pop(0)
            prio.pop(0)
            th += 1
        else:
            docu.append(docu.pop(0))
            prio.append(prio.pop(0))
