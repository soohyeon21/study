# 31067

import sys

n, k = map(int, sys.stdin.readline().split())
an = list(map(int, sys.stdin.readline().split()))

cnt = 0
state = True
for i in range(n-1):
    if (an[i] < an[i+1]):
        pass
    elif (an[i] < an[i+1]+k):
        an[i+1] += k
        cnt +=1
    else:
        state = False # cnt = -1로 만들든가.
        break

if (state):
    print(cnt)
else:
    print(-1)
