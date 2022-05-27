# 5575

import sys

for _ in range(3):
    work = list(map(int, sys.stdin.readline().split()))
    arrive = work[0]*60*60 + work[1]*60 + work[2]
    leave = work[3]*60*60 + work[4]*60 + work[5]
    time = leave - arrive
    print(time//60**2, (time//60)%60, time%60)
