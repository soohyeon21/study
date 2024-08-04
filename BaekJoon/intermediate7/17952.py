# 17952

# IndexError 방지를 위해서 yet을 의미없는 값으로 채워줬다.

# ipt[0]=1일때 yet에 append하고, if (yet)일때 pop 및 작업하는 방법도 있다.

import sys

n = int(sys.stdin.readline())

score = 0
yet = [(0, 1) for _ in range(n)]
for _ in range(n):
    ipt = list(map(int, sys.stdin.readline().split()))
    now_score, remain_time = 0, 0

    if (ipt[0] == 0):
        now_score, remain_time = yet.pop()
        remain_time -= 1
    elif (ipt[0] == 1):
        now_score = ipt[1]
        remain_time = ipt[2]-1
        
    if (remain_time == 0):
        score += now_score
    else:
        yet.append((now_score, remain_time))

print(score)
