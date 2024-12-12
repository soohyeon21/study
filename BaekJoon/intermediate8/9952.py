# 9952

# deque(), append(), appendleft()를 사용하는 방법도 있다.

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break
    
    can = {}
    for _ in range(n):
        code, height = sys.stdin.readline().split()
        can[code] = int(height)

    order = sorted(can.items(), key=lambda x:(-x[1], x[0].lower()))

    pantry = [order[0][0]]
    for i in range(1, n):
        if (i % 2 != 0):
            pantry.insert(0, order[i][0])
        else:
            pantry.append(order[i][0])

    print(*pantry)
