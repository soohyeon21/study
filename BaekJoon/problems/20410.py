# 20410

# a와 c를 그냥 하나씩 확인하면서 x1과 x2가 나오는지 확인하는, 단순한 방법도 있다.

import sys

m, seed, x1, x2 = map(int, sys.stdin.readline().split())

answer = []
state = False
for m1 in range(2*m):
    for m2 in range(2*m):
        a1 = x1 + m*m1
        a2 = x2 + m*m2
        
        if (seed-x1 != 0):
            a = (a1-a2)/(seed-x1)
            c = a1 - seed*a
            if ((a == int(a)) and (0 <= a < m) and (int(c) == c) and (0 <= c < m)):
                answer = [int(a), int(c)]
                state = True
        else:
            for a in range(m):
                for c in range(m):
                    if (seed*a + c == x1 + m*m1):
                        answer = [int(a), int(c)]
                        state = True

                    if (state):
                        break
                if (state):
                    break

        if (state):
            break
    if (state):
        break

print(*answer)
