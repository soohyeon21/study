# 23881

import sys

n, k = map(int, sys.stdin.readline().split())
an = list(map(int, sys.stdin.readline().split()))

cnt = 0
state = False
mm, mx = 0, 0
for last in reversed(range(1, n)):
    i = an.index(max(an[:last+1]))
    if (i != last):
        cnt += 1
        an[last], an[i] = an[i], an[last]
        if (cnt == k):
            state = True
            mm, mx = min(an[last], an[i]), max(an[last], an[i])
            break

if (state):
    print(mm, mx)
else:
    print(-1)
