# 18141

# if ((i == j) or (j == k) or (i == k)): continue # 한 번에 처리도 가능

import sys

n = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))

state = True
for i in range(n):
    for j in range(n):
        if (j == i):
            continue
        for k in range(n):
            if ((k == i) or (k == j)):
                continue
            if ((an[i]-an[j])/an[k] != int((an[i]-an[j])/an[k])):
                state = False

if (state):
    print('yes')
else:
    print('no')
