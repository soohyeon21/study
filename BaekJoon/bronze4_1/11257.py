# 11257

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    ID, *test = map(int, sys.stdin.readline().split())
    
    state = True
    
    thr = [35, 25, 40]
    for i in range(3):
        if (test[i] < thr[i]*0.3):
            state = False
            
    if (sum(test) < 55):
        state = False

    print(ID, sum(test), ['FAIL', 'PASS'][state])
